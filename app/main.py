from fastapi import FastAPI
from app.models import SearchRequest
from app.engine import search_similar

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Similarity Engine Running"}

@app.post("/search")
def search(req: SearchRequest):
    results = search_similar(req.query, req.top_k)
    return {"results": results}