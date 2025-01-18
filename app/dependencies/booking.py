from fastapi import HTTPException
from app.dependencies.db import get_db
from app.dependencies.books import BookOperations
from sqlalchemy.orm import Session
from app.models.bookings import Booking
from datetime import datetime


book_operation = BookOperations()

class BookingOperations:

    def __init__(self) -> None:
        self.db: Session = next(get_db())
    

    def get_booking(self, booking_id: int = None):
        if not booking_id:
            return self.db.query(Booking).all()
        
        booking = self.db.query(Booking).filter(Booking.id == booking_id).first()

        if not booking:
            raise HTTPException(status_code=404, detail="Booking not found")
        
        return booking
    
    def add_booking(self, booking):
        try:
        
         book = book_operation.get_book(booking.book_id)

         if not book:
             raise HTTPException(status_code=404, detail={ 'message':'error','detail' : 'Book not found. Please enter available book id'})

         new_booking = Booking(book_id = booking.book_id, users_id = booking.users_id,
                            approved = 0 ) #by default approved is zero
         
         self.db.add(new_booking)
         self.db.commit()
         self.db.refresh(new_booking)  

        except:
            self.db.rollback()
            raise HTTPException(status_code=500,detail="Error reserving the book")
        
        book_instance = book_operation.get_book()

        return { 'message': 'success', 'data':new_book }
