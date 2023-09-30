"""The main entrypoint for the application"""
from fastapi import FastAPI

app = FastAPI(
    title="Second Hand Cars",
    description="The backend of a second hand cars app",
    version="0.1.0"
)


@app.get("/")
async def root() -> dict[str, str]:
    """The root endpoint"""
    return {"message": "Hello World"}
