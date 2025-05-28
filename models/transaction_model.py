import json
from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional, Union
import re
import pandas as pd

from models.customer_model import Gender, CustomerModel
from utils.constants import Constants
from utils.csv_reader import CSVFileUtils


@dataclass
class TransactionModel:
    def __init__(
            self,
            order_id: int,
            order_date: date,
            days_since_purchase: int,
            customer_id: int,
            customer_age: int,
            customer_gender: Optional[Gender],
            product_name: str,
            product_id: int,
            quantity: int,
            price: float,
            coupon_code: str,
            shipping_city: str,
            discounted_price: float,

    ):
        self.order_id = order_id
        self.order_date = order_date
        self.days_since_purchase = days_since_purchase
        self.customer_id = customer_id
        self.customer_age= customer_age
        self.customer_gender= customer_gender
        self.product_name = product_name
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.discounted_price = discounted_price
        self.coupon_code = coupon_code
        self.shipping_city = shipping_city

    @classmethod
    def from_raw_data(cls, raw: dict) -> "TransactionModel":
        return TransactionModel(
            order_id=raw.get("order_id"),
            order_date=raw.get("order_date"),
            days_since_purchase=raw.get("days_since_purchase", 0),
            customer_id=raw.get("customer_id"),
            customer_age=raw.get("customer_age", 0),
            customer_gender=raw.get("customer_gender"),
            product_name=raw.get("product_name"),
            product_id=raw.get("product_id"),
            quantity=raw.get("quantity"),
            price=raw.get("price"),
            discounted_price=raw.get("discounted_price", 0.0),
            coupon_code=raw.get("coupon_code"),
            shipping_city=raw.get("shipping_city"),
        )

    @staticmethod
    def load_transactions() -> list["TransactionModel"]:
        transactions: list[TransactionModel] = []
        raw_data = CSVFileUtils.read_csv_with_rage(file_path=Constants.synth_generated_csv_file_path())
        for row in raw_data:
            transactions.append(TransactionModel.from_raw_data(row))

        return transactions

    def clean(self) -> Optional["TransactionModel"]:
        def clean_string(value: str) -> str:
            if not isinstance(value, str):
                return ""
            value = value.strip()
            value = re.sub(r'[^a-zA-Z0-9\s]', '', value)  # Remove special characters
            value = re.sub(r'\s+', ' ', value)  # Remove multiple spaces
            return value.title()  # Uppercase

        # Clean the string fields in the model
        cleaned_product_name = clean_string(self.product_name)
        cleaned_shipping_city = clean_string(self.shipping_city)
        cleaned_coupon_code = self.coupon_code.strip() if isinstance(self.coupon_code, str) else ""

        def parse_date(value: Union[str, date]) -> Union[date, None]:
            if isinstance(value, date):
                return value
            if not isinstance(value, str):
                return None

            value = value.strip()
            date_formats = [
                "%m/%d/%Y",
                "%m-%d-%Y",
                "%d-%m-%Y",
                "%Y-%m-%d"
            ]
            for fmt in date_formats:
                try:
                    return datetime.strptime(value, fmt).date()
                except ValueError:
                    continue
            return None

        cleaned_order_date = parse_date(self.order_date)

        # Convert price to float, handling errors
        try:
            cleaned_price = float(self.price)
        except (ValueError, TypeError):
            return None

        # Convert quantity to float, handling errors
        try:
            cleaned_quantity = int(self.quantity)
        except (ValueError, TypeError):
            return None

        # Return new instance
        return TransactionModel(
            order_id=self.order_id,
            order_date=cleaned_order_date,
            customer_id=self.customer_id,
            product_name=cleaned_product_name,
            product_id=self.product_id,
            quantity=cleaned_quantity,
            price=cleaned_price,
            coupon_code=cleaned_coupon_code,
            shipping_city=cleaned_shipping_city,
            discounted_price=0.0,  # Will be calculated later
            days_since_purchase=0,  # Will be calculated later
            customer_age=0,  # will be added later
            customer_gender=None,  # will be added later
        )

    def calculate_discount(self) -> None:
        # I am considering a simple condition for discount calculation that is the length of
        # clean coupon code must be>10 characters. A valid coupon will have 10% discount.
        if len(self.coupon_code) > 10:
            self.discounted_price = self.price * 0.9
        else:
            self.discounted_price = self.price

    def calculate_days_since_purchase(self) -> None:
        if isinstance(self.order_date, date):
            today = date.today()
            self.days_since_purchase = (today - self.order_date).days

    def to_dict(self) -> dict:
        obj_dict = self.__dict__.copy()
        obj_dict['order_date'] = self.order_date.isoformat()
        return obj_dict

    def save_transactions_to_json_file(self: list["TransactionModel"]) -> None:
        list_of_dicts = [txn.to_dict() for txn in self]

        with open(Constants.cleaned_json_file_path(), 'w') as f:
            json.dump(list_of_dicts, f, indent=4)

    def save_transactions_to_parquet(self: list["TransactionModel"]) -> None:
        list_of_dicts = [txn.to_dict() for txn in self]

        df = pd.DataFrame(list_of_dicts)
        df.to_parquet(Constants.cleaned_parquet_file_path(), index=False, engine="pyarrow")

    def add_customer_info(self, c: Optional[CustomerModel]):
            self.customer_age = int(c.age)
            self.customer_gender = c.gender
