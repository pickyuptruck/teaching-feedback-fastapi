from fastapi import FastAPI
from models import Lesson


app = FastAPI()


@app.get("/lessons")
async def get_lessons():
    return {"message": "GET lessons"}

@app.get("/lessons/{lesson_id}")
async def get_lesson(lesson_id: int):
    return {"lesson_id": lesson_id}

@app.post("/lessons")
async def create_lesson():
    return {"message": "create lessons"}

@app.delete("/lessons/{lesson_id}")
async def delete_lesson(lesson_id: int):
    return {"lesson_id": lesson_id}