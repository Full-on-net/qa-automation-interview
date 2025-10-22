from app.database import users, orders

def _next_user_id() -> int:
    return len(users)

def _next_order_id() -> int:
    return len(orders)

def add_user(user: dict) -> dict:
    new_user = {"id": _next_user_id(), **user}
    users.append(new_user)
    return new_user

def get_user(user_id: int) -> dict | None:
    for u in users:
        if u["id"] == user_id:
            return u
    return None

def get_all_users() -> list[dict]:
    return users

def add_order(order: dict) -> dict:
    new_order = {"id": _next_order_id(), **order}
    orders.append(new_order)
    return new_order

def get_all_orders() -> list[dict]:
    return orders

def get_orders_by_user(user_id: int) -> list[dict]:
    return [o for o in orders if o["user_id"] == user_id]