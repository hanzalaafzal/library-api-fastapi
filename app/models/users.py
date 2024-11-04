from sqlalchemy import Column, Integer, String
from app.dependencies.db import Base

class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=False)
    email = Column(String, unique=True, index=True)
    password = Column(String)  
    role = Column(Integer)  
    