from AI_feature.scoring import (
    calculate_skill_match,
    calculate_interest_match,
    calculate_goal_match,
    calculate_semantic_match,
    calculate_final_score
)


required_skills = [
    "Python",
    "Machine Learning",
    "React"
]

student_skills = [
    "Python",
    "Machine Learning",
    "Pandas"
]


skill_score = calculate_skill_match(
    required_skills,
    student_skills
)

print("Skill Match:", skill_score)


project_interests = [
    "AI",
    "Healthcare"
]

student_interests = [
    "AI",
    "Healthcare"
]

interest_score = calculate_interest_match(
    project_interests,
    student_interests
)

print("Interest Match:", interest_score)


project_goal = "Build an AI healthcare project"

student_goals = [
    "AI projects",
    "Healthcare technology"
]

goal_score = calculate_goal_match(
    project_goal,
    student_goals
)

print("Goal Match:", goal_score)


project_text = """
AI healthcare platform using Python
and machine learning.
"""

student_text = """
Student experienced in Python,
machine learning and healthcare AI.
"""

semantic_score = calculate_semantic_match(
    project_text,
    student_text
)

print("Semantic Match:", semantic_score)


experience_score = 80

final_score = calculate_final_score(
    skill_score,
    semantic_score,
    interest_score,
    goal_score,
    experience_score
)
assert skill_score > 60, f"Expected high skill match, got {skill_score}"
print("Final Match Score:", final_score)