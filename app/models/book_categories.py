from sqlalchemy import Column, Integer, String
from app.dependencies.db import Base

class BookCategory(Base):
    
    __tablename__ = "book_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String,unique=True,index=True,nullable=False)
    