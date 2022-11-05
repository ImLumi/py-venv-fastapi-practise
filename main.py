from fastapi import FastAPI

from src.messure_place import router

app = FastAPI()
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Halihó!"}
