from datetime import date,datetime
from typing import Optional
from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    slug:str
    released_on:date
    version:int
    description:str
    author_id: int
    category_id: int
    created_at: Optional[datetime] = datetime.utcnow()
    available: int

class BookUpdate(BaseModel):
    title: str
    slug:str
    released_on:date
    version:int
    description:str
    author_id: int
    category_id: int
    available: int
    updated_at: Optional[datetime] = datetime.utcnow()