class Constants:
    @staticmethod
    def customer_csv_file_path() -> str:
            return 'data/customer.csv'

    @staticmethod
    def sales_record_csv_file_path() -> str:
            return 'data/1000_sales_records.csv'

    @staticmethod
    def fashion_products_csv_file_path() -> str:
            return 'data/fashion_products.csv'

    @staticmethod
    def synth_generated_csv_file_path() -> str:
            return 'data/transactions_generated.csv'

    @staticmethod
    def cleaned_json_file_path() -> str:
            return 'data/cleaned/transactions_cleaned.json'

    @staticmethod
    def cleaned_parquet_file_path() -> str:
            return 'data/cleaned/transactions_cleaned_parquet.parquet'