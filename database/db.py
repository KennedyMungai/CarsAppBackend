"""The database config file"""
from beanie import init_beanie
import motor.motor_asyncio
from models.models import Car


async def init_db():
    """The application to talk with the database"""
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017")
    await init_beanie(database=client.Cars, document_models=[Car])
