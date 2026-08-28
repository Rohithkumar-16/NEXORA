from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from database import engine, get_db, Base
import models, schemas
from ai_matcher import match_candidates_for_project

# Create all tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(title="NEXORA Backend API")

# Allow the frontend teammate to connect with no blockers
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

<<<<<<< HEAD
# 1. Create a Student Profile
@app.post("/api/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 2. Get All Student Profiles
@app.get("/api/users", response_model=List[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# 3. Create a Project
@app.post("/api/projects", response_model=schemas.ProjectOut)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# 4. Get All Projects
@app.get("/api/projects", response_model=List[schemas.ProjectOut])
def get_projects(db: Session = Depends(get_db)):
    return db.query(models.Project).all()

# 5. AI Teammate Matching Engine
@app.get("/api/projects/{project_id}/recommendations", response_model=List[schemas.MatchResult])
def get_recommendations(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    users = db.query(models.User).all()
    return match_candidates_for_project(project, users)

# 6. Create Workspace Task
@app.post("/api/tasks", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.WorkspaceTask(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# 7. Get Workspace Tasks for a Project
@app.get("/api/projects/{project_id}/tasks", response_model=List[schemas.TaskOut])
def get_tasks(project_id: int, db: Session = Depends(get_db)):
    return db.query(models.WorkspaceTask).filter(models.WorkspaceTask.project_id == project_id).all()
=======
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
>>>>>>> 74b0f77397b08f78fd8ce97090fea33b7f2bd58e
