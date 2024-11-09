from pydantic import BaseModel


class Authors(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True