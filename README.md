# **Synopsis**
This project aims at collecting and pre-processing data for AI and ML applications.
I have collected data from 3 datasets and written a function to produce a synthetic dataset 
which matches the assignment requirements. This generated dataset(transactions_generated.csv) is the main dataset I have used.
Then I have written classes and methods to ingest, clean and transform the data.

# **Quick-start**
1.  Run `python -m venv venv` to create a virtual environment.
2.  Run `source venv/bin/activate` to activate the virtual environment.
3.  Run `pip install -r requirements.txt` to install the dependencies.
4. Click **Run-All** in the Jupyter Notebook to run all the cells.

# **Data Sources**
1. [1000_sales_records.csv](https://excelbianalytics.com/wp/wp-content/uploads/2017/07/1000-Sales-Records.zip) - sales dataset
2. [customer.csv](https://www.kaggle.com/datasets/bhadramohit/customer-shopping-latest-trends-dataset) - customer data
3. [fashion_products](https://www.kaggle.com/datasets/bhanupratapbiswas/fashion-products) - products dataset
4. transactions_generated.csv - synthetic dataset generated using the `generate_synthetic_data` method in `SyntheticDataUtils` class in `utils/synthetic_data_utils.py`
