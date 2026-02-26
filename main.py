from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from parser import parse_query

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/execute")
def execute(q: str = Query(...)):
    result = parse_query(q)
    return result