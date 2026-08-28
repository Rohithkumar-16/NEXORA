from AI_feature.embeddings import calculate_similarity


def calculate_skill_match(required_skills, student_skills):
    """
    Calculate how many required skills
    the student has.
    """

    required = {
        skill.lower().strip()
        for skill in required_skills
    }

    student = {
        skill.lower().strip()
        for skill in student_skills
    }

    if not required:
        return 0

    matched = required.intersection(student)

    score = (len(matched) / len(required)) * 100

    return round(score, 2)


def calculate_interest_match(project_interests, student_interests):
    """
    Calculate the percentage of project interests
    that match the student's interests.
    """

    project = {
        interest.lower().strip()
        for interest in project_interests
    }

    student = {
        interest.lower().strip()
        for interest in student_interests
    }

    if not project:
        return 0

    matched = project.intersection(student)

    score = (len(matched) / len(project)) * 100

    return round(score, 2)


def calculate_goal_match(project_goal, student_goals):
    """
    Compare project goal with student's goals
    using semantic similarity.
    """

    student_goal_text = " ".join(student_goals)

    similarity = calculate_similarity(
        project_goal,
        student_goal_text
    )

    return round(similarity * 100, 2)


def calculate_semantic_match(project_text, student_text):
    """
    Compare the complete project and student
    information using semantic similarity.
    """

    similarity = calculate_similarity(
        project_text,
        student_text
    )

    return round(similarity * 100, 2)


def calculate_final_score(
    skill_score,
    semantic_score,
    interest_score,
    goal_score,
    experience_score
):
    """
    Calculate final compatibility score.
    """

    final_score = (
        skill_score * 0.40 +
        semantic_score * 0.25 +
        interest_score * 0.15 +
        goal_score * 0.10 +
        experience_score * 0.10
    )

    return round(final_score, 2)