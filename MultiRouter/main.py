from fastapi import FastAPI
from books.router import router as books_router
from users.router import router as users_router

# Create the main FastAPI application
app = FastAPI(title="Multi-Router Example")

# Register routers into the main app
app.include_router(books_router)
app.include_router(users_router)

@app.get("/")
def root():
    return {"message": "Welcome to Multi-Router Example API"}
