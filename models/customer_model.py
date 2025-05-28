from enum import Enum

class Gender(Enum):
    MALE = 1
    FEMALE = 2

    @classmethod
    def from_string(cls, value: str) -> "Gender":
            if value.lower().strip() == Gender.MALE.name.lower(): return  Gender.MALE
            return  Gender.FEMALE

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

    # def print_sample(self): print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Blood Type: {self.blood_type}, Medical Condition: {self.medical_condition}, Date of Admission: {self.date_of_admission}, Doctor: {self.doctor}, Hospital: {self.hospital}, Insurance Provider: {self.insurance_provider}, Billing Amount: {self.billing_amount}, Room Number: {self.room_number}, Admission Type: {self.admission_type}, Discharge Date: {self.discharge_date}, Medication: {self.medication}, Test Results: {self.test_results}")



