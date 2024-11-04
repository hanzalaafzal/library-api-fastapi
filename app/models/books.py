from sqlalchemy import Column, Integer, String, ForeignKey,Date,DateTime
from app.dependencies.db import Base
from datetime import datetime



class Book(Base):
    
    __tablename__ = "books"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, index = True)
    category_id = Column(Integer,ForeignKey("book_categories.id"), nullable = False)
    slug = Column(String,unique = True,index = True, nullable = False)
    released_on = Column(Date, nullable = False)
    version = Column(Integer, default = 1)
    description = Column(Integer,nullable = False,default = "Lorem Ipsum Lorem Ipsum")
    available = Column(Integer)
    created_at = Column(DateTime, default = datetime.utcnow())
    author_id = Column(Integer, ForeignKey("authors.id"), nullable = False)
    