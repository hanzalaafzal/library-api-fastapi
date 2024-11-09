from sqlalchemy import Column, Integer, String
from app.dependencies.db import Base
from sqlalchemy.orm import relationship

class Author(Base):
    
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Integer,nullable=False,default="Lorem Ipsum Lorem Ipsum")

    books = relationship("Book", back_populates="author")