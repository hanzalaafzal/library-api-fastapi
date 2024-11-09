from fastapi import HTTPException
from app.dependencies.db import get_db
from app.dependencies.book_category import BookCategoryOperations
from sqlalchemy.orm import Session
from app.models.books import Book
from app.models.book_categories import BookCategory
from app.schemas.books import BookResponse

category_operations = BookCategoryOperations()


class BookOperations:


    def __init__(self):
        self.db: Session = next(get_db())

    def get_book(self,book_id: int = None):
        
        if not book_id:
            return self.db.query(Book).all()
        
        book = self.db.query(Book).filter(Book.id == book_id).first()

        return book

    
    def list_books(self, book_id: int = None):
        if not book_id:
            return { 'message': 'success', 
                    'data':[BookResponse.model_validate(book) for book in self.get_book(self,book_id)] }
        
        book = self.db.query(Book).filter(Book.id == book_id).first()
        
        if not book:
            raise HTTPException(status_code=404, detail={ 'message':'error','detail' : 'book not found'})

        return { 'message': 'success', 
                'data': [BookResponse.model_validate(book)] }



    def add_book(self,book):
        
        try:
            book_category = category_operations.get_category(book.category_id)

            new_book = Book(title = book.title, category_id = book.category_id,
                     released_on = book.released_on, slug = book.slug,
                     version = book.version, description = book.description,
                     created_at = book.created_at, available = book.available,
                     author_id = book.author_id
                     )
        
            self.db.add(new_book)
            self.db.commit()
            self.db.refresh(new_book)

            new_book.update('category', book_category)

        except:
            self.db.rollback()
            raise HTTPException(status_code=500,
                                detail={ 'message': 'error', 'detail' : 'Error adding book' , 'data':new_book })

        return { 'message': 'success', 'data':new_book }
    
    def update_book(self,book_id: int ,book):
        
        existing_book = self.get_book(book_id)
        
        existing_book.title = book.title or existing_book.title

        self.db.commit()
        
        self.db.refresh(existing_book)
        
        return existing_book
    
    def get_book_category(self):
        return self.db.query(BookCategory).all()