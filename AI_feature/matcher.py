from AI_feature.scoring import (
    calculate_skill_match,
    calculate_interest_match,
    calculate_goal_match,
    calculate_semantic_match,
    calculate_final_score
)


def build_project_text(project):
    """
    Convert project information into one text block
    for semantic comparison.
    """

    return f"""
    Project title:
    {project['title']}

    Description:
    {project['description']}

    Required skills:
    {', '.join(project['required_skills'])}

    Technologies:
    {', '.join(project['technologies'])}

    Interests:
    {', '.join(project['interests'])}

    Goal:
    {project['goal']}
    """


def build_student_text(student):
    """
    Convert student information into one text block
    for semantic comparison.
    """

    return f"""
    Student:
    {student['name']}

    Skills:
    {', '.join(student['skills'])}

    Interests:
    {', '.join(student['interests'])}

    Goals:
    {', '.join(student['goals'])}

    Experience:
    {student['experience']} projects
    """


def generate_reasons(
    skill_score,
    semantic_score,
    interest_score,
    goal_score
):
    """
    Generate human-readable reasons for the match.
    """

    reasons = []

    if skill_score >= 70:
        reasons.append("Strong required-skill match")
    elif skill_score >= 40:
        reasons.append("Partial required-skill match")

    if semantic_score >= 70:
        reasons.append("Strong semantic compatibility")

    if interest_score >= 70:
        reasons.append("Interests align with the project")

    if goal_score >= 70:
        reasons.append("Project goals align with student's goals")

    return reasons


def match_student_to_project(project, student):
    """
    Calculate compatibility between one student
    and one project.
    """

    project_text = build_project_text(project)
    student_text = build_student_text(student)

    skill_score = calculate_skill_match(
        project["required_skills"],
        student["skills"]
    )

    interest_score = calculate_interest_match(
        project["interests"],
        student["interests"]
    )

    goal_score = calculate_goal_match(
        project["goal"],
        student["goals"]
    )

    semantic_score = calculate_semantic_match(
        project_text,
        student_text
    )

    # Convert experience into a score.
    # 5+ projects = 100.
    experience_score = min(
        student["experience"] * 20,
        100
    )

    final_score = calculate_final_score(
        skill_score,
        semantic_score,
        interest_score,
        goal_score,
        experience_score
    )

    reasons = generate_reasons(
        skill_score,
        semantic_score,
        interest_score,
        goal_score
    )

    return {
        "student_id": student["id"],
        "student_name": student["name"],
        "score": final_score,

        "breakdown": {
            "skill": skill_score,
            "semantic": semantic_score,
            "interest": interest_score,
            "goal": goal_score,
            "experience": experience_score
        },

        "reasons": reasons
    }


def find_matches(project, students, top_k=5):
    """
    Find and rank the best students for a project.
    """

    results = []

    for student in students:

        result = match_student_to_project(
            project,
            student
        )

        results.append(result)

    # Highest score first
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_k]