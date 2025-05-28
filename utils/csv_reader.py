import csv

class CSVFileUtils:
    @staticmethod
    def read_csv_with_rage(file_path: str, start: int =1, end: int =None)->list[dict[str, str]]:
        dirty_list = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = list(csv.DictReader(csv_file))
            total_rows = len(reader)

            if end is None or end > total_rows:
                end = total_rows

            dirty_list = reader[start-1:end]

        return dirty_list

    @staticmethod
    def save_csv_to_file(file_path: str, csv_data: list[dict[str, str]], **kwargs) -> None:
        fieldnames = csv_data[0].keys()
        with open(file_path, mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames, **kwargs)
            writer.writeheader()
            writer.writerows(csv_data)