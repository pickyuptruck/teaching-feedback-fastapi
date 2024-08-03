from sqlalchemy import Column, String
from sqlalchemy.types import UUID
from uuid import uuid4
from .database import Base


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(UUID, primary_key=True, default=uuid4)
    title = Column(String, default="New lesson")
    transcript = Column(String, nullable=True)
    feedback = Column(String, nullable=True) 
