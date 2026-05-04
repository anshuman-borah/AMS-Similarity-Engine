# AMS Similarity Engine

## Setup
1. Create virtual env
2. Install dependencies:
   pip install -r requirements.txt

3. Run:
   uvicorn app.main:app --reload

## API
POST /search
{
  "query": "text"
}