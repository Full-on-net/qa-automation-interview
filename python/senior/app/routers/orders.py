from fastapi import APIRouter
from app.schemas import Order, OrderCreate
from app.crud import create_order, fetch_all_orders, fetch_orders_by_user
from app.crud import fetch_user  # Para posible validación (no usada intencionadamente)

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("", response_model=list[Order])
def list_orders():
    return fetch_all_orders()

@router.post("", response_model=Order, status_code=201)
def create_order_endpoint(payload: OrderCreate):
    created = create_order(
        user_id=payload.user_id,
        product=payload.product,
        quantity=payload.quantity,
        price=payload.price,  
    )
    return created

@router.get("/{user_id}", response_model=list[Order])
def list_orders_for_user(user_id: int):
    return fetch_orders_by_user(user_id)