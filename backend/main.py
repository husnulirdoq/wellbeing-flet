import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db_tasks = []

class Task(BaseModel):
    content: str

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
    # Render bakal kasih nomor port otomatis lewat env variable PORT
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)