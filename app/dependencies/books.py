from fastapi import HTTPException
from app.dependencies.db import get_db
from sqlalchemy.orm import Session
from app.models.books import Book
from app.models.book_categories import BookCategory
from app.models.authors import Author 
from datetime import datetime


class BookOperations:


    def __init__(self):
        self.db: Session = next(get_db())

    def get_book(self,book_id: int):
        if not book_id:
            return self.db.query(Book).all()
        
        book = self.db.query(Book).filter(Book.id == book_id).first()

        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        return book

    def add_book(self,book):
        
        try:

            new_book = Book(title=book.title, category_id=book.category_id,
                     released_on=book.released_on, slug=book.slug,
                     version=book.version, description=book.description,
                     created_at = book.created_at, available = book.available,
                     author_id = book.author_id
                     )
        
            self.db.add(new_book)
            self.db.commit()
            self.db.refresh(new_book)

        except:
            self.db.rollback()
            raise HTTPException(status_code=500,detail="Error Adding Data")

        return { 'message': 'success', 'data':new_book }
    
    def update_book(self,book_id,book):
        existing_book = self.db.query(Book).filter(Book.id == book_id).first()
        
        if not existing_book:
            raise HTTPException(status_code=404, detail="Book not found")
        
        existing_book.title = book.title or existing_book.title
        self.db.commit()
        self.db.refresh(existing_book)
        
        return existing_book
    
    def get_book_category(self):
        return self.db.query(BookCategory).all()