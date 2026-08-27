from sentence_transformers import SentenceTransformer


# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text):
    """
    Convert text into a numerical vector.
    """
    embedding = model.encode(text)
    return embedding


def calculate_similarity(text1, text2):
    """
    Calculate semantic similarity between two texts.
    Returns a value between 0 and 1.
    """

    embeddings = model.encode([text1, text2])

    similarity = model.similarity(
        embeddings[0],
        embeddings[1]
    )

    return float(similarity.item())