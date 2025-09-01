from fastapi import APIRouter

# Create a router for book-related endpoints
router = APIRouter(prefix="/books", tags=["books"])

# Example endpoint: GET /books/
@router.get("/")
def list_books():
    return [
        {"id": 1, "title": "1984", "author": "George Orwell"},
        {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"}
    ]

# Example endpoint: GET /books/{book_id}
@router.get("/{book_id}")
def get_book(book_id: int):
    return {"id": book_id, "title": "Dummy Book", "author": "Unknown"}
