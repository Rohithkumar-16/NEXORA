from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from AI_feature.search import search_students
from AI_feature.matcher import find_matches
from data.dummy_data import students, project


app = FastAPI(
    title="ALEROPATH AI API",
    description="AI Search and Matching Engine",
    version="1.0"
)


# =========================
# SEARCH
# =========================

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5


@app.post("/ai/search")
def ai_search(request: SearchRequest):

    results = search_students(
        request.query,
        students,
        request.top_k
    )

    return {
        "query": request.query,
        "results": results
    }


# =========================
# MATCHING
# =========================

class MatchRequest(BaseModel):
    top_k: int = 5


@app.post("/ai/match")
def ai_match(request: MatchRequest):

    matches = find_matches(
        project,
        students,
        request.top_k
    )

    return {
        "project": project["title"],
        "matches": matches
    }


# =========================
# HEALTH CHECK
# =========================

@app.get("/")
def home():

    return {
        "status": "running",
        "service": "ALEROPATH AI"
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten to your actual frontend URL before real deployment
    allow_methods=["*"],
    allow_headers=["*"],
)