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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, Any, Tuple, List

def evaluate_evidence(domain: str, metrics: Dict[str, Any]) -> Tuple[str, float, List[str]]:
    """
    Analyzes evidence metrics per domain, computes confidence score (0-100%),
    assigns domain progression level, and generates verification badges.
    """
    confidence = 10.0  # Base confidence
    badges = []
    level = "Beginner"

    domain_lower = domain.lower()

    if "competitive" in domain_lower or "programming" in domain_lower:
        leetcode = int(metrics.get("leetcode_rating", 0) or 0)
        codeforces = int(metrics.get("codeforces_rating", 0) or 0)
        problems = int(metrics.get("problems_solved", 0) or 0)

        if leetcode > 0 or codeforces > 0:
            confidence += 35
            badges.append("Competitive Platform Verified")
        if problems >= 100:
            confidence += 25
            badges.append(f"{problems}+ Problems Solved")
        if leetcode >= 1800 or codeforces >= 1500:
            confidence += 25
            level = "Advanced"
            badges.append("High Contest Rating")
        elif leetcode >= 1500 or problems >= 200:
            level = "Intermediate"
        elif problems > 30:
            level = "Practitioner"

    elif "ai" in domain_lower or "ml" in domain_lower or "machine learning" in domain_lower:
        gh_repos = int(metrics.get("github_ml_repos", 0) or 0)
        kaggle_medals = int(metrics.get("kaggle_medals", 0) or 0)
        hf_models = int(metrics.get("hf_models", 0) or 0)

        sources = sum(1 for x in [gh_repos, kaggle_medals, hf_models] if x > 0)
        if sources >= 2:
            confidence += 40
            badges.append("Multi-Source AI Evidence")
        elif sources == 1:
            confidence += 20

        if gh_repos >= 5:
            confidence += 20
            badges.append(f"{gh_repos} Open-Source ML Repos")
        if kaggle_medals >= 1 or hf_models >= 2:
            confidence += 25
            level = "Advanced"
            badges.append("Published Models / Kaggle Proof")
        elif gh_repos >= 3:
            level = "Intermediate"
        elif gh_repos >= 1:
            level = "Practitioner"

    elif "design" in domain_lower or "ui" in domain_lower or "ux" in domain_lower:
        behance = int(metrics.get("behance_projects", 0) or 0)
        dribbble = int(metrics.get("dribbble_shots", 0) or 0)
        portfolio = bool(metrics.get("has_portfolio", False))

        if portfolio:
            confidence += 30
            badges.append("Portfolio Verified")
        if behance >= 5 or dribbble >= 5:
            confidence += 35
            badges.append("Active Design Profiles")
        
        total_projects = behance + dribbble
        if total_projects >= 15:
            level = "Advanced"
            confidence += 20
        elif total_projects >= 5:
            level = "Intermediate"
        elif total_projects >= 1:
            level = "Practitioner"

    else:
        # Generic Domain Scoring
        repo_count = int(metrics.get("repos", 0) or 0)
        if repo_count > 0:
            confidence += min(repo_count * 10, 60)
            badges.append(f"{repo_count} Public Projects")
            level = "Practitioner" if repo_count < 5 else "Intermediate"

    final_confidence = min(confidence, 98.0)
    return level, round(final_confidence, 1), badges


def calculate_match_score(
    project_text: str,
    project_skills: str,
    required_domain: str,
    user_text: str,
    user_skills: str,
    user_profiles: list
) -> Tuple[float, Optional[str], str, float, List[str]]:
    """
    Computes match score factoring semantic NLP fit + verified evidence confidence.
    """
    # 1. Semantic Cosine Similarity
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([project_text, user_text])
    content_sim = float(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0])

    # 2. Skill Tag Overlap (Jaccard)
    proj_skills_set = set(s.strip().lower() for s in project_skills.split(",") if s.strip())
    user_skills_set = set(s.strip().lower() for s in user_skills.split(",") if s.strip())
    
    if proj_skills_set:
        overlap = proj_skills_set.intersection(user_skills_set)
        skill_sim = len(overlap) / len(proj_skills_set)
    else:
        skill_sim = 0.5

    # 3. Domain Verification Lookup
    matched_profile = None
    if user_profiles:
        for profile in user_profiles:
            if required_domain.lower() in profile.domain.lower() or profile.domain.lower() in required_domain.lower():
                matched_profile = profile
                break
        if not matched_profile:
            matched_profile = user_profiles[0]

    domain_name = matched_profile.domain if matched_profile else required_domain
    domain_level = matched_profile.level if matched_profile else "Unverified"
    confidence = matched_profile.confidence_score if matched_profile else 10.0
    highlights = matched_profile.verification_badges if matched_profile else ["Self-claimed skills (Unverified)"]

    # 4. Final Weighted Score: 40% NLP Fit + 30% Skill Overlap + 30% Evidence Confidence
    total_score = (content_sim * 40.0) + (skill_sim * 30.0) + ((confidence / 100.0) * 30.0)
    
    return round(total_score, 2), domain_name, domain_level, confidence, highlights
