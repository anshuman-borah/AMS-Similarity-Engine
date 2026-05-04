from fastapi import FastAPI
from pydantic import BaseModel
from app.engine import search_similar

app = FastAPI()


class ProposalInput(BaseModel):
    title: str = ""
    description: str = ""
    objectives: str = ""
    methodology: str = ""


@app.get("/")
def home():
    return {"message": "Similarity Engine Running"}


@app.post("/search")
def search(data: ProposalInput):
    query = f"""
    {data.title} {data.title}
    {data.description}
    {data.objectives}
    {data.methodology}
    """

    return search_similar(query)