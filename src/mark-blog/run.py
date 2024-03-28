from fastapi import FastAPI
from main import blog_app

app = blog_app(FastAPI())

@app.get("/")
async def index() -> dict:
    return {
        "message": "Visit the blog at",
        "url": "http://localhost:8000/blog",
    }