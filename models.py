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