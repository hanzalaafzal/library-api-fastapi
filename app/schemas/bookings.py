from pydantic import BaseModel


class BookingCreate(BaseModel):
    book_id: int
    users_id: int
    approved:int

class BookingUpdate(BaseModel):
    approved:int