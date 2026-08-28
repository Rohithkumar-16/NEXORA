from AI_feature.search import search_students
from data.dummy_data import students


query = """
I need a student who knows Python and machine learning
and is interested in healthcare and artificial intelligence.
"""


results = search_students(
    query,
    students,
    top_k=5
)


print("\n==============================")
print("        NEXORA AI SEARCH")
print("==============================\n")


print("Query:")
print(query)


print("\nResults:\n")


for index, result in enumerate(results, start=1):

    print(
        f"{index}. "
        f"{result['student_name']} "
        f"→ {result['score']}%"
    )