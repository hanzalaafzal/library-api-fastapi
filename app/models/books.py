from sqlalchemy import Column, Integer, String, ForeignKey,Date,DateTime
from app.dependencies.db import Base
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.authors import Author
from app.models.bookings import Booking



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
    

    category = relationship("BookCategory", back_populates = "books")
    author = relationship("Author",back_populates = "books")
    booking = relationship("Booking", back_populates="book")