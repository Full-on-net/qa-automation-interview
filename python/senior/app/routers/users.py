from fastapi import APIRouter
from app.schemas import User, UserCreate
from app.crud import create_user, fetch_all_users

router = APIRouter(prefix="/users", tags=["users"])

@router.get("", response_model=list[User])
def list_users():
    return fetch_all_users()

@router.post("", response_model=User, status_code=201)
def create_user_endpoint(payload: UserCreate):
    created = create_user(name=payload.name, email=payload.email)
    return created