from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import engine, get_db
from ai_matcher import evaluate_evidence, calculate_match_score

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NEXORA - Skill Verification & Teammate Engine",
    description="Transforms scattered student achievements into verified, domain-specific reputations.",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to NEXORA Reputation Engine API"}

# --- Users Endpoints ---
@app.post("/api/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/api/users", response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# --- Skill Verification & Profile Ingestion Endpoint ---
@app.post("/api/verify-profile", response_model=schemas.SkillProfileResponse)
def verify_and_add_profile(profile_data: schemas.SkillProfileCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == profile_data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Run verification analysis
    level, confidence, badges = evaluate_evidence(profile_data.domain, profile_data.metrics)

    skill_profile = models.SkillProfile(
        user_id=profile_data.user_id,
        domain=profile_data.domain,
        level=level,
        confidence_score=confidence,
        metrics=profile_data.metrics,
        verification_badges=badges
    )
    db.add(skill_profile)
    db.commit()
    db.refresh(skill_profile)
    return skill_profile

# --- Projects Endpoints ---
@app.post("/api/projects", response_model=schemas.ProjectResponse)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    new_project = models.Project(**project.model_dump())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@app.get("/api/projects", response_model=List[schemas.ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    return db.query(models.Project).all()

# --- Evidence-Based Matchmaking Endpoint ---
@app.get("/api/projects/{project_id}/recommendations", response_model=List[schemas.CandidateMatch])
def get_recommended_candidates(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    users = db.query(models.User).filter(models.User.id != project.creator_id).all()
    project_text = f"{project.title} {project.description} {project.required_skills}"

    candidates = []
    for u in users:
        user_text = f"{u.bio} {u.skills}"
        score, domain, level, confidence, badges = calculate_match_score(
            project_text=project_text,
            project_skills=project.required_skills,
            required_domain=project.required_domain,
            user_text=user_text,
            user_skills=u.skills,
            user_profiles=u.skill_profiles
        )

        candidates.append(
            schemas.CandidateMatch(
                user_id=u.id,
                name=u.name,
                bio=u.bio,
                skills=[s.strip() for s in u.skills.split(",") if s.strip()],
                matched_domain=domain,
                domain_level=level,
                evidence_confidence=confidence,
                match_score=score,
                verification_highlights=badges
            )
        )

    # Sort highest match score first
    candidates.sort(key=lambda x: x.match_score, reverse=True)
    return candidates