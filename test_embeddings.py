from AI_feature.embeddings import calculate_similarity


text1 = """
Python machine learning artificial intelligence healthcare
"""

text2 = """
I am interested in AI and medical technology.
I have experience with Python and machine learning.
"""

text3 = """
I like graphic design, photography and video editing.
"""


similarity1 = calculate_similarity(text1, text2)
similarity2 = calculate_similarity(text1, text3)


print("AI/Healthcare similarity:", similarity1)
print("AI/Design similarity:", similarity2)