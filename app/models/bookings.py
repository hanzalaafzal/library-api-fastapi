from sqlalchemy import Column, Integer,ForeignKey,Boolean
from app.dependencies.db import Base
from sqlalchemy.orm import relationship

class Booking(Base):
    
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    users_id = Column(Integer, ForeignKey("users.id"))
    approved = Column(Boolean, default=0)
    
    book = relationship("Book", back_populates = "booking")
    user = relationship("User", back_populates = "booking" )