from datetime import date,datetime
from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    slug:str
    released_on:date
    version:int
    description:str
    author_id: int
    created_at:datetime

class BookUpdate(BaseModel):
    title: str
    slug:str
    released_on:date
    version:int
    description:str
    author_id: int