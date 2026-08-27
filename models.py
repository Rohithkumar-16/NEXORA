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
from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    bio = Column(String)
    skills = Column(String)  # Comma-separated tags
    overall_reputation = Column(Float, default=0.0)

    # Relationships
    skill_profiles = relationship("SkillProfile", back_populates="user", cascade="all, delete-orphan")
    projects_created = relationship("Project", back_populates="creator")

class SkillProfile(Base):
    __tablename__ = "skill_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    domain = Column(String, index=True)       # e.g., "AI / ML", "Competitive Programming", "UI/UX Design"
    level = Column(String, default="Beginner") # Beginner, Practitioner, Intermediate, Advanced, Expert
    confidence_score = Column(Float, default=0.0)  # 0 to 100%
    
    # Evidence & Platform Data (JSON dictionary)
    # e.g., {"github_repos": 8, "kaggle_medals": 2, "leetcode_rating": 1850, "behance_projects": 12}
    metrics = Column(JSON, default=dict)
    
    # Verification checks summary (JSON list)
    # e.g., ["Multiple sources found", "Consistent activity detected"]
    verification_badges = Column(JSON, default=list)

    user = relationship("User", back_populates="skill_profiles")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    required_domain = Column(String, default="General")
    required_skills = Column(String)  # Comma-separated tags
    creator_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="projects_created")
