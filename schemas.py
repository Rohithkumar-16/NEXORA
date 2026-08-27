from pydantic import BaseModel
from typing import Optional

# Format for creating a user
class UserCreate(BaseModel):
    name: str
    email: str
    college: str
    semester: str
    bio: str
    skills: str
    interests: str
    experience_level: str
    availability_hrs: int

# Format for returning a user
class UserOut(UserCreate):
    id: int
    class Config:
        from_attributes = True

# Format for creating a project
class ProjectCreate(BaseModel):
    owner_id: int
    title: str
    problem_statement: str
    description: str
    required_skills: str
    tech_stack: str

# Format for returning a project
class ProjectOut(ProjectCreate):
    id: int
    status: str
    class Config:
        from_attributes = True

# Format for AI Matching output
class MatchResult(BaseModel):
    user_id: int
    name: str
    email: str
    skills: str
    match_score: float
    match_reason: str

# Format for tasks
class TaskCreate(BaseModel):
    project_id: int
    title: str
    status: str = "todo"

class TaskOut(TaskCreate):
    id: int
    class Config:
        from_attributes = True