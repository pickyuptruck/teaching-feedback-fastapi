from uuid import UUID
from pydantic import BaseModel

class Lesson(BaseModel):
    id: UUID
    name: str
    description: str
    transcript: str
    feedback: str
    