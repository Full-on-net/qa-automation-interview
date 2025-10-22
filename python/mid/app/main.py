from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Buggy Task API Challenge")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Buggy Task API"}