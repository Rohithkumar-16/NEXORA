from sentence_transformers import SentenceTransformer, util

# Load the AI sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def match_candidates_for_project(project, candidate_users):
    recommendations = []
    
    # 1. Prepare project text description
    project_text = f"{project.title} {project.problem_statement} {project.description}"
    project_embedding = model.encode(project_text, convert_to_tensor=True)
    
    req_skills = set([s.strip().lower() for s in project.required_skills.split(",") if s.strip()])
    
    for candidate in candidate_users:
        if candidate.id == project.owner_id:
            continue  # Don't recommend the project owner to themselves
        
        # Calculate Skill Match (50% weight)
        user_skills = set([s.strip().lower() for s in candidate.skills.split(",") if s.strip()])
        shared_skills = user_skills.intersection(req_skills)
        skill_score = (len(shared_skills) / len(req_skills) * 100) if req_skills else 0
        
        # Calculate Semantic Meaning Match (30% weight)
        candidate_text = f"{candidate.bio} {candidate.interests}"
        candidate_embedding = model.encode(candidate_text, convert_to_tensor=True)
        semantic_sim = util.cos_sim(project_embedding, candidate_embedding).item()
        semantic_score = max(0.0, semantic_sim) * 100
        
        # Calculate Availability Match (20% weight)
        avail_score = min(candidate.availability_hrs / 20.0, 1.0) * 100
        
        # Total Final Score
        final_score = round((0.50 * skill_score) + (0.30 * semantic_score) + (0.20 * avail_score), 1)
        
        # Generate clear reason for judges
        reason = f"Matches skills: {', '.join(shared_skills)}" if shared_skills else "High semantic match with project theme"
        
        recommendations.append({
            "user_id": candidate.id,
            "name": candidate.name,
            "email": candidate.email,
            "skills": candidate.skills,
            "match_score": final_score,
            "match_reason": reason
        })
        
    # Sort highest score first
    recommendations.sort(key=lambda x: x["match_score"], reverse=True)
    return recommendations