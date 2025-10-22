from pydantic import BaseModel, Field

# Nota: Schemas expuestos en la API (entrada/salida)

class User(BaseModel):
    id: int
    name: str
    email: str

class UserCreate(BaseModel):
    name: str = Field(min_length=1)
    email: str

class Order(BaseModel):
    id: int
    user_id: int
    product: str
    quantity: int
    price: float  

class OrderCreate(BaseModel):
    user_id: int
    product: str = Field(min_length=1)
    quantity: int
    price: float  