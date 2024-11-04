from pydantic import BaseModel

class Authentication(BaseModel):
    email: str
    password: str