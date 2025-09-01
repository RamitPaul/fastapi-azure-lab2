from fastapi import APIRouter

# Create a router for user-related endpoints
router = APIRouter(prefix="/users", tags=["users"])

# Example endpoint: GET /users/
@router.get("/")
def list_users():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]

# Example endpoint: GET /users/{user_id}
@router.get("/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "name": "Dummy User"}
