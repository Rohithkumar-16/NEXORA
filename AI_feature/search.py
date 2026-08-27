from AI_feature.embeddings import create_embedding
from sklearn.metrics.pairwise import cosine_similarity


def build_student_search_text(student):
    """
    Convert a student's profile into searchable text.
    """

    return f"""
    Student name: {student['name']}

    Skills:
    {', '.join(student['skills'])}

    Interests:
    {', '.join(student['interests'])}

    Goals:
    {', '.join(student['goals'])}

    Experience:
    {student['experience']} projects
    """


def search_students(query, students, top_k=5):
    """
    Search students using natural language.
    """

    # Convert user's query into an embedding
    query_embedding = create_embedding(query)

    results = []

    for student in students:

        student_text = build_student_search_text(student)

        # Convert student profile into embedding
        student_embedding = create_embedding(
            student_text
        )

        # Calculate semantic similarity
        similarity = cosine_similarity(
            [query_embedding],
            [student_embedding]
        )[0][0]

        score = round(
            float(similarity) * 100,
            2
        )

        results.append({
            "student_id": student["id"],
            "student_name": student["name"],
            "score": score
        })

    # Highest similarity first
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_k]