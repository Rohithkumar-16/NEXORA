from database import SessionLocal, engine, Base
import models

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Clear old entries
db.query(models.WorkspaceTask).delete()
db.query(models.Project).delete()
db.query(models.User).delete()

# Create Sample Students
u1 = models.User(
    name="Aarav Sharma", email="aarav@marwadi.edu", college="Marwadi University",
    semester="3rd Sem AI-DS", bio="Focused on Deep Learning, NLP, and building backend APIs.",
    skills="Python, FastAPI, PyTorch, SQL", interests="GenAI, NLP, Backend Dev",
    experience_level="Intermediate", availability_hrs=15
)
u2 = models.User(
    name="Priya Patel", email="priya@marwadi.edu", college="Marwadi University",
    semester="5th Sem CE", bio="Building modern UI/UX using React and Tailwind.",
    skills="React, JavaScript, TailwindCSS, Next.js", interests="UI/UX, Web Design",
    experience_level="Advanced", availability_hrs=20
)
u3 = models.User(
    name="Rohan Mehta", email="rohan@marwadi.edu", college="Marwadi University",
    semester="3rd Sem IT", bio="Cloud enthusiast and backend developer learning Docker.",
    skills="Docker, Linux, AWS, Git, Python", interests="Cloud, DevOps",
    experience_level="Beginner", availability_hrs=8
)

db.add_all([u1, u2, u3])
db.commit()

# Create Sample Project
proj = models.Project(
    owner_id=u2.id,
    title="MedAssist - AI Medical Bot",
    problem_statement="Hospitals have long triage delays. We need an automated clinical triage assistant.",
    description="Building a conversational AI bot with Python backend and React front dashboard.",
    required_skills="Python, FastAPI, PyTorch",
    tech_stack="FastAPI, PyTorch, React",
    status="open"
)
db.add(proj)
db.commit()

# Create Sample Task
t1 = models.WorkspaceTask(project_id=proj.id, title="Set up FastAPI Backend", status="done")
t2 = models.WorkspaceTask(project_id=proj.id, title="Integrate Sentence-Transformers", status="todo")
db.add_all([t1, t2])
db.commit()

print("--> Database populated successfully with realistic sample data!")
db.close() 
from ai_matcher import evaluate_evidence

# Safely drop and recreate all tables
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

print("🌱 Seeding Users, Verified Domain Profiles, and Projects...")

# 1. Create Users
user_rohit = models.User(
    name="Rohith Kumar",
    email="rohith@example.com",
    bio="AI Researcher specializing in NLP and Computer Vision with PyTorch and Hugging Face.",
    skills="Python, PyTorch, Transformers, Computer Vision, Machine Learning"
)
user_ananya = models.User(
    name="Ananya Sharma",
    email="ananya@example.com",
    bio="Competitive programmer and backend developer interested in scalable algorithms.",
    skills="C++, Algorithms, LeetCode, Fast I/O, Data Structures"
)
user_kevin = models.User(
    name="Kevin Patel",
    email="kevin@example.com",
    bio="Product designer focused on clean Figma workflows, design systems, and micro-interactions.",
    skills="Figma, UI/UX, Prototyping, Design Systems, Mobile Design"
)

db.add_all([user_rohit, user_ananya, user_kevin])
db.commit()

# 2. Add Evidence Profiles
profiles = [
    {
        "user": user_rohit,
        "domain": "AI / Machine Learning",
        "metrics": {"github_ml_repos": 8, "kaggle_medals": 2, "hf_models": 3}
    },
    {
        "user": user_ananya,
        "domain": "Competitive Programming",
        "metrics": {"leetcode_rating": 1850, "codeforces_rating": 1510, "problems_solved": 680}
    },
    {
        "user": user_kevin,
        "domain": "UI/UX Design",
        "metrics": {"behance_projects": 12, "dribbble_shots": 8, "has_portfolio": True}
    }
]

for p in profiles:
    lvl, conf, badges = evaluate_evidence(p["domain"], p["metrics"])
    sp = models.SkillProfile(
        user_id=p["user"].id,
        domain=p["domain"],
        level=lvl,
        confidence_score=conf,
        metrics=p["metrics"],
        verification_badges=badges
    )
    db.add(sp)

db.commit()

# 3. Create Sample Projects
project_ai = models.Project(
    title="AI Healthcare Diagnostic Assistant",
    description="Building a deep learning multi-modal pipeline to analyze medical imagery and patient notes.",
    required_domain="AI / Machine Learning",
    required_skills="Python, PyTorch, Transformers, Computer Vision",
    creator_id=user_kevin.id
)

project_algo = models.Project(
    title="High-Frequency Order Matching Engine",
    description="Designing low-latency algorithmic trade routing using memory-efficient structures.",
    required_domain="Competitive Programming",
    required_skills="C++, Algorithms, Data Structures",
    creator_id=user_rohit.id
)

db.add_all([project_ai, project_algo])
db.commit()
db.close()

print("✅ Seed completed successfully with verified domain reputations!")
