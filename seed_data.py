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