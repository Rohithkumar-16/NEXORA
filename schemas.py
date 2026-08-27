from pydantic import BaseModel
from typing import List, Dict, Any, Optional

# --- Skill Profile & Verification Schemas ---
class SkillProfileBase(BaseModel):
    domain: str
    metrics: Dict[str, Any]

class SkillProfileCreate(SkillProfileBase):
    user_id: int

class SkillProfileResponse(BaseModel):
    id: int
    domain: str
    level: str
    confidence_score: float
    metrics: Dict[str, Any]
    verification_badges: List[str]

    class Config:
        from_attributes = True

# --- User Schemas ---
class UserBase(BaseModel):
    name: str
    email: str
    bio: str
    skills: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    overall_reputation: float
    skill_profiles: List[SkillProfileResponse] = []

    class Config:
        from_attributes = True

# --- Project Schemas ---
class ProjectBase(BaseModel):
    title: str
    description: str
    required_domain: Optional[str] = "General"
    required_skills: str

class ProjectCreate(ProjectBase):
    creator_id: int

class ProjectResponse(ProjectBase):
    id: int
    creator_id: int

    class Config:
        from_attributes = True

# --- Match / Recommendation Response ---
class CandidateMatch(BaseModel):
    user_id: int
    name: str
    bio: str
    skills: List[str]
    matched_domain: Optional[str] = None
    domain_level: Optional[str] = "Unverified"
    evidence_confidence: float
    match_score: float
    verification_highlights: List[str]