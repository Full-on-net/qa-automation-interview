# Simulación de "base de datos" en memoria
# Contiene funciones básicas para operar con usuarios y pedidos.

users = [
    {"id": 0, "name": "Alice", "email": "alice@example.com"},
    {"id": 1, "name": "Bob", "email": "bob@example.com"},
    {"id": 2, "name": "Charlie", "email": "charlie@example.com"},
    {"id": 3, "name": "David", "email": "david@example.com"},
    {"id": 4, "name": "Eve", "email": "eve@example.com"},
]

orders = [
    {"id": 0, "user_id": 0, "product": "Book", "quantity": 1, "price": 9.99},
    {"id": 1, "user_id": 1, "product": "Pen", "quantity": 3, "price": 1.50},
    {"id": 2, "user_id": 2, "product": "Notebook", "quantity": 1, "price": 12.50},
    {"id": 3, "user_id": 4, "product": "Calculator", "quantity": 1, "price": 20.00},
    {"id": 4, "user_id": 4, "product": "Pencil", "quantity": 5, "price": 0.50},
]

def get_user(user_id: int) -> dict | None:
    for u in users:
        if u["id"] == user_id:
            return u
    return None

def get_all_users() -> list[dict]:
    return users

def get_all_orders() -> list[dict]:
    return orders

def get_orders_by_user(user_id: int) -> list[dict]:
    return [o for o in orders if o["user_id"] == user_id]