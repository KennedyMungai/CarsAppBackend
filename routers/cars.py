"""The second hand cars route"""
from typing import List

from fastapi import APIRouter

from models.models import Car
from beanie import PydanticObjectId

cars_router = APIRouter(prefix="/cars", tags=["Cars"])


@cars_router.get("/")
async def get_all_second_hand_cars() -> List[Car]:
    """The endpoint to retrieve all the cars from the database"""
    cars = await Car.find_all().to_list()
    return cars


@cars_router.get("/{car_id}")
async def get_single_car_by_id(car_id: PydanticObjectId) -> Car:
    """The endpoint to retrieve a single car by id"""
    car = await Car.find_one(car_id)
    return car
