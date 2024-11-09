from pydantic import BaseModel


class BookCategory(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True