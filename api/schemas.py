from pydantic import BaseModel
from uuid import UUID

class LessonBase(BaseModel):
    transcript: str | None = None
    feedback: str | None = None


class LessonCreate(LessonBase):
    pass


class Lesson(LessonBase):
    id: UUID
    title: str

    class Config:
        orm_mode = True
