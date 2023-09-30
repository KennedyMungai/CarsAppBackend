"""The second hand cars route"""
from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status

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

    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Car entry not found"
        )

    return car


@cars_router.post("/", status_code=status.HTTP_201_CREATED, )
async def create_car(car: Car) -> Car:
    """The endpoint to create a car"""
    try:
        await car.create()
        return car
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Car entry already exists")
