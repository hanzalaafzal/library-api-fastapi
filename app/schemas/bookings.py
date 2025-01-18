from typing import List
from pydantic import BaseModel
from app.schemas.books import BookResponse
from app.schemas.users import UserBase

class BookingCreate(BaseModel):
    book_id: int
    users_id: int
    approved:int

class BookingUpdate(BaseModel):
    approved:int


class BookingResponse(BaseModel):

    user: UserBase
    book : BookResponse
    approved: int
    
    class Config:
        from_attributes = True

class BookingApiResponse(BaseModel):
    message: str
    data: List[BookingResponse]