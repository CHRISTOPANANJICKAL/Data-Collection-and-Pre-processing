import random

from models.customer_model import CustomerModel
from models.product_model import ProductModel
from models.sales_model import SalesModel
from models.transaction_model import TransactionModel
from utils.constants import Constants
from utils.csv_reader import CSVFileUtils


class SyntheticDataUtils:
    @staticmethod
    def generate_synthetic_data() -> None:

            # Read the 3 CSV files
            customer_csv_data: list[dict[str, str]] = (
                CSVFileUtils.read_csv_with_rage(file_path=Constants.customer_csv_file_path(), start=1))

            sales_csv_data: list[dict[str, str]] = (
                CSVFileUtils.read_csv_with_rage(file_path=Constants.sales_record_csv_file_path(), start=1))

            products_csv_data: list[dict[str, str]] = (
                CSVFileUtils.read_csv_with_rage(file_path=Constants.fashion_products_csv_file_path(), start=1))


            # Convert the customer data to CustomerModel instances
            customer_list: list[CustomerModel] = []
            for i in customer_csv_data:
                customer_list.append(CustomerModel.from_raw_data(i))

            # Convert the product data to ProductModel instances
            product_list: list[ProductModel] = []
            for i in products_csv_data:
                product_list.append(ProductModel.from_raw_data(i))

            # Convert the sales data to SalesModel instances
            sales_list: list[SalesModel] = []
            for i in sales_csv_data:
                sales_list.append(SalesModel.from_raw_data(i))


            # Generate synthetic transactions records
            transaction_list: list[TransactionModel] = []


            # Add fake customer IDs and product IDs to the sales records
            for sales in sales_list:
                customer = customer_list[random.randint(0, len(customer_list)-1)]
                product = product_list[random.randint(0, len(product_list)-1)]

                must_have_coupon = random.choice([True, False, False, False, False])
                # Add a simple fake coupon code on random basis
                coupon_code = 'Hooray!! 342AHR' if must_have_coupon else ''

                transaction_list.append(
                    TransactionModel(
                        order_id=sales.order_id,
                        order_date=sales.order_date,
                        customer_id=customer.customer_id,
                        product_name=product.name,
                        product_id=product.product_id,
                        quantity=sales.quantity,
                        price=product.price,
                        coupon_code=coupon_code,
                        shipping_city=customer.location
                    )
                )

            # Convert the transaction model instances into a list of dictionaries for CSV writing
            transactions_csv_data = [{k: str(v) for k, v in vars(t).items()} for t in transaction_list]

            CSVFileUtils.save_csv_to_file(file_path=Constants.synth_generated_csv_file_path(),csv_data=transactions_csv_data)