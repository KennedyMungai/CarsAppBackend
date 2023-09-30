"""The second hand cars route"""
from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter

from models.models import Car

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


@cars_router.post("/")
async def create_car(car: Car) -> Car:
    """The endpoint to create a car"""
    await car.create()
    return car
