"""The main entrypoint for the application"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.db import init_db
from routers.cars import cars_router

app = FastAPI(
    title="Second Hand Cars",
    description="The backend of a second hand cars app",
    version="0.1.0"
)

origins = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://localhost",
    "https://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
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


app.include_router(cars_router)
