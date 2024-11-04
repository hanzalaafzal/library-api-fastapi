from sqlalchemy import Column, Integer,ForeignKey,Boolean
from app.dependencies.db import Base

class Booking(Base):
    
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    student_id = Column(Integer, ForeignKey("users.id"))
    approved = Column(Boolean, default=0)
    