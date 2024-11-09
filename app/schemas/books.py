from datetime import date,datetime
from typing import Optional
from pydantic import BaseModel
from app.schemas.book_category import BookCategory
from app.schemas.author import Authors
from typing import List


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


class BookResponse(BaseModel):
    id: int
    title: str
    slug: str
    released_on: date
    version: int
    description: str
    author: Authors
    available: Optional[int]
    category: BookCategory

    class Config:
        from_attributes = True

class BookApiResponse(BaseModel):
    message:str
    data: List[BookResponse]

    class Config:
        from_attributes = True