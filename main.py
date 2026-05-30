from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/to_upper")
def to_upper(text: str):
    """Convert a query parameter 'text' to upper case."""
    return {"original": text, "upper": text.upper()}