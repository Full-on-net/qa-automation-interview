from app.utils.utils import (
    add_user,
    get_user,
    get_all_users,
    add_order,
    get_all_orders,
    get_orders_by_user,
)

# Capa CRUD: orquesta la lógica de acceso a "DB".
# Nota: se dejan intencionadamente algunas validaciones sin implementar.

def create_user(name: str, email: str) -> dict:
    payload = {"name": name, "email": email}
    return add_user(payload)

def fetch_user(user_id: int) -> dict | None:
    return get_user(user_id)

def fetch_all_users() -> list[dict]:
    return get_all_users()

def create_order(user_id: int, product: str, quantity: int, price: str) -> dict:
    payload = {"user_id": user_id, "product": product, "quantity": quantity, "price": float(price) if price.replace('.', '', 1).isdigit() else price}
    return add_order(payload)

def fetch_all_orders() -> list[dict]:
    return get_all_orders()

def fetch_orders_by_user(user_id: int) -> list[dict]:
    return get_orders_by_user(user_id)