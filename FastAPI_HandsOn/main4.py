from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

app = FastAPI(title="Book Management API - Custom Validation")

class Book(BaseModel):
    id: int = Field(..., gt=0, description="Book ID must be positive")
    title: str = Field(..., min_length=3, max_length=100, description="Book title (3–100 chars)")
    author: str = Field(..., min_length=3, description="Author name (min 3 chars)")
    price: float = Field(..., gt=0, lt=5000, description="Price must be between 0 and 5000")
    published_year: Optional[int] = Field(
        None, ge=1900, le=9999, description="Year must be between 1900 and current year"
    )

    @field_validator("title")
    def title_must_start_with_capital(cls, value):
        if not value[0].isupper():
            raise ValueError("Title must start with a capital letter")
        return value

    @field_validator("price")
    def price_warning(cls, value):
        if value > 1000:
            logging.warning(f"High price detected: {value}. Consider reviewing the price.")
        return value

    @field_validator("published_year")
    def year_not_in_future(cls, value):
        if value is not None and value > datetime.now().year:
            raise ValueError("Published year cannot be greater than the current year")
        return value

books_db: List[Book] = [
    Book(id=1, title="Harry Potter", author="J.K.Rowling", price=499.99, published_year=2001),
    Book(id=2, title="The Hobbit", author="J.R.R. Tolkien", price=399.50, published_year=1937),
]

@app.get("/")
def home():
    return {"message": "Welcome to Book Management API - Custom Validation"}

@app.get("/books", response_model=List[Book])
def get_books():
    return books_db

@app.post("/books", response_model=Book)
def add_book(book: Book):
    books_db.append(book)
    return book
