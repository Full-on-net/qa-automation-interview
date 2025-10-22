from pydantic import BaseModel

# Nota: Estos modelos representan la forma interna de almacenamiento (DB en memoria).
# Los esquemas (request/response) están en schemas.py.

class UserModel(BaseModel):
    id: int
    name: str
    email: str

class OrderModel(BaseModel):
    id: int
    user_id: int
    product: str
    quantity: int
    price: float