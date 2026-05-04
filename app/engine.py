from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from app.data import get_documents

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load documents
documents = get_documents()

if len(documents) == 0:
    raise ValueError("No documents available for similarity search")

# Create embeddings
doc_embeddings = model.encode(documents)

# FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add vectors (convert to float32)
index.add(np.array(doc_embeddings).astype("float32"))


def search_similar(query: str, top_k: int = 3):
    query_vector = np.array(model.encode([query])).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = []

    for i, idx in enumerate(indices[0]):
        distance = float(distances[0][i])
        score = 1 / (1 + distance)

        results.append({
            "text": documents[int(idx)],
            "score": round(score * 100, 2)
        })

    return results