from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    MALE = 1
    FEMALE = 2

    @classmethod
    def from_string(cls, value: str) -> "Gender":
            if value.lower().strip() == Gender.MALE.name.lower(): return  Gender.MALE
            return  Gender.FEMALE

@dataclass
class CustomerModel:
    def __init__(
        self,
        customer_id: int,
        age:int,
        gender:Gender,
        location:str,
    ):
        self.customer_id = customer_id
        self.age = age
        self.gender = gender
        self.location = location


    @classmethod
    def from_raw_data(cls,raw: dict) -> "CustomerModel":
        return CustomerModel(
            customer_id=raw.get("Customer ID"),
            age=raw.get("Age"),
            gender=raw.get("Gender"),
            location=raw.get("Location"),
        )






