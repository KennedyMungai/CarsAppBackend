"""The second hand cars route"""
from typing import List

from fastapi import APIRouter

from models.models import Car

cars_router = APIRouter(prefix="/cars", tags=["Cars"])


@cars_router.get("/")
async def get_all_second_hand_cars() -> List[Car]:
    """The endpoint to retrieve all the cars from the database"""
    cars = await Car.all()
    return cars
