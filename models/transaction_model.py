from datetime import date

class TransactionModel:
    def __init__(
        self,
        order_id: int,
        order_date: date,
        customer_id: int,
        product_name: str,
        product_id: int,
        quantity: int,
        price: float,
        coupon_code:str,
        shipping_city: str,
    ):
        self.order_id = order_id
        self.order_date = order_date
        self.customer_id = customer_id
        self.product_name = product_name
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.coupon_code = coupon_code
        self.shipping_city = shipping_city

    # @classmethod
    # def from_raw_data(cls,raw: dict) -> "TransactionModel":
    #     return TransactionModel(
    #         order_id=raw.get("Order ID"),
    #         order_date=raw.get("Order Date"),
    #         shipping_date=raw.get("Ship Date"),
    #         quantity=raw.get("Units Sold"),
    #     )