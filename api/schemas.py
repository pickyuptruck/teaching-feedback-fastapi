from pydantic import BaseModel
from uuid import UUID

class LessonBase(BaseModel):
    title: str
    transcript: str | None = None
    feedback: str | None = None


class LessonCreate(LessonBase):
    pass


class Lesson(LessonBase):
    id: UUID

    class Config:
        orm_mode = True
