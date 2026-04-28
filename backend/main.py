import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS udah bener, ini krusial biar Flet bisa akses
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db_tasks = []

class Task(BaseModel):
    content: str

@app.get("/")
def read_root():
    return {"message": "API is running on Hugging Face!"}

@app.get("/tasks")
def get_tasks():
    return db_tasks

@app.post("/tasks")
def add_task(task: Task):
    db_tasks.append(task.content)
    return {"status": "success"}

@app.delete("/tasks/{idx}")
def delete_task(idx: int):
    if 0 <= idx < len(db_tasks):
        db_tasks.pop(idx)
        return {"status": "deleted"}
    return {"status": "error"}

if __name__ == "__main__":
    # GANTI DISINI: Hugging Face default port itu 7860
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)