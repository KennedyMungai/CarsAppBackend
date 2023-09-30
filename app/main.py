"""The main entrypoint for the application"""
from fastapi import FastAPI
from database.db import init_db

app = FastAPI(
    title="Second Hand Cars",
    description="The backend of a second hand cars app",
    version="0.1.0"
)


@app.on_event("startup")
async def database_connection():
    """The function to connect to the database on startup"""
    print("Connecting to database...")
    await init_db()


@app.get("/")
async def root() -> dict[str, str]:
    """The root endpoint"""
    return {"message": "Hello World"}
