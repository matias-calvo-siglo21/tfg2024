from fastapi import FastAPI
from app.routers import router

app = FastAPI()

app.include_router(router.router)

@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}

