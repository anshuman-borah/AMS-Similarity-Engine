from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from app.data import get_documents

documents = get_documents()

model = SentenceTransformer('all-MiniLM-L6-v2')

doc_embeddings = model.encode(documents)

dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

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
            "score": round(float(score) * 100, 2)
        })

    return results