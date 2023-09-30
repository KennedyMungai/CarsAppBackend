"""The models for the application"""
from typing import Optional

from beanie import Document
from pydantic import BaseModel


class Car(Document):
    """The car model"""
    brand: str
    make: str
    year: int
    price: int
    km: int
    cm3: int

    class Settings:
        """The settings for the car model"""
        name = "second_hand_cars"

    class Config:
        """The config for the car model"""
        json_schema_extra = {
            "example": {
                "brand": "Mercedes",
                "make": "Some pretentious words",
                "year": 1999,
                "price": 999999,
                "km": 999999,
                "cm3": 999999
            }
        }


class CarUpdate(BaseModel):
    """The car update model"""
    price: Optional[int] = None
