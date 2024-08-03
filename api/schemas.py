from pydantic import BaseModel
from uuid import UUID

class ItemBase(BaseModel):
    title: str
    transcript: str | None = None
    feedback: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: UUID

    class Config:
        orm_mode = True
