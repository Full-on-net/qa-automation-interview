from fastapi import FastAPI
from app.routers.users import router as users_router
from app.routers.orders import router as orders_router

app = FastAPI(title="Buggy E-Commerce API Challenge")

# Routers
app.include_router(users_router)
app.include_router(orders_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Buggy E-Commerce API"}