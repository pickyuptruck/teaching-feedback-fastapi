from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/lessons/", response_model=list[schemas.Lesson])
def read_lessons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lessons = crud.get_lessons(db, skip=skip, limit=limit)
    return lessons

@app.get("/lessons/{lesson_id}")
async def get_lesson(lesson_id: int):
    return {"lesson_id": lesson_id}

@app.post("/lessons")
async def create_lesson():
    return {"message": "create lessons"}

@app.delete("/lessons/{lesson_id}")
async def delete_lesson(lesson_id: int):
    return {"lesson_id": lesson_id}