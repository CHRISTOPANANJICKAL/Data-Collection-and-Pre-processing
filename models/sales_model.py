from dataclasses import dataclass
from datetime import date

@dataclass
class SalesModel:
    def __init__(
        self,
        order_id: int,
        order_date: date,
        shipping_date:date,
        quantity: int,
    ):
        self.order_id = order_id
        self.order_date = order_date
        self.shipping_date = shipping_date
        self.quantity = quantity


    @classmethod
    def from_raw_data(cls,raw: dict) -> "SalesModel":
        return SalesModel(
            order_id=raw.get("Order ID"),
            order_date=raw.get("Order Date"),
            shipping_date=raw.get("Ship Date"),
            quantity=raw.get("Units Sold"),
        )