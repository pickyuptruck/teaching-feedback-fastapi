from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from .database import Base


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(UUID, primary_key=True)
    title = Column(String, default="New lesson")
    transcript = Column(String, nullable=True)
    feedback = Column(String, nullable=True) 
