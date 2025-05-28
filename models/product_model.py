from dataclasses import dataclass


@dataclass
class ProductModel:
    def __init__(
        self,
        product_id: int,
        name:str,
        brand:str,
        price:float,
    ):
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.price = price


    @classmethod
    def from_raw_data(cls,raw: dict) -> "ProductModel":
        return ProductModel(
            product_id=raw.get("Product ID"),
            name=raw.get("Product Name"),
            brand=raw.get("Brand"),
            price=raw.get("Price"),
        )

    # def print_sample(self): print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Blood Type: {self.blood_type}, Medical Condition: {self.medical_condition}, Date of Admission: {self.date_of_admission}, Doctor: {self.doctor}, Hospital: {self.hospital}, Insurance Provider: {self.insurance_provider}, Billing Amount: {self.billing_amount}, Room Number: {self.room_number}, Admission Type: {self.admission_type}, Discharge Date: {self.discharge_date}, Medication: {self.medication}, Test Results: {self.test_results}")

