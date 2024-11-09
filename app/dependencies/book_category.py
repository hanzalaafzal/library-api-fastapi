from fastapi import HTTPException
from app.dependencies.db import get_db
from sqlalchemy.orm import Session
from app.models.book_categories import BookCategory

# we are just assuming we have data in book_category tables
# no api to add book category considering we have already categories in table

class BookCategoryOperations:

    def __init__(self):
        self.db: Session = next(get_db())
    
    def get_category(self, category_id: int = None):
        
        if not category_id:
            return self.db.query(BookCategory).all()
        
        book_category = self.db.query(BookCategory).filter(BookCategory.id == category_id).first()

        if not book_category:
            raise HTTPException(status_code=404, detail="Book category not found")

        return book_category