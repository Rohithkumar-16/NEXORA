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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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