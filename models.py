from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base

# Table for Student Profiles
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    college = Column(String)
    semester = Column(String)
    bio = Column(Text)
    skills = Column(Text)              # Example: "Python, FastAPI, SQL"
    interests = Column(Text)           # Example: "AI, FinTech"
    experience_level = Column(String)  # Beginner / Intermediate / Advanced
    availability_hrs = Column(Integer, default=10)

# Table for Projects
class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    problem_statement = Column(Text)
    description = Column(Text)
    required_skills = Column(Text)     # Example: "Python, React"
    tech_stack = Column(String)
    status = Column(String, default="open")

# Table for Workspace Tasks
class WorkspaceTask(Base):
    __tablename__ = "workspace_tasks"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    title = Column(String, nullable=False)
    status = Column(String, default="todo") # todo / in_progress / done