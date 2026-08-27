from AI_feature.matcher import find_matches
from data.dummy_data import students, project


matches = find_matches(
    project,
    students,
    top_k=5
)


print("\n==============================")
print("       NEXORA AI MATCHING")
print("==============================\n")


for index, match in enumerate(matches, start=1):

    print(
        f"{index}. "
        f"{match['student_name']} "
        f"→ {match['score']}%"
    )

    print("\nReasons:")

    for reason in match["reasons"]:
        print("  ✓", reason)

    print("\nScore Breakdown:")

    for key, value in match["breakdown"].items():
        print(f"  {key}: {value}%")

    print("\n" + "-" * 40)