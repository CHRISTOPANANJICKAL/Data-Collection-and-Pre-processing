from collections import defaultdict
from typing import Optional, Any, Dict

from models.transaction_model import TransactionModel


class ArithmeticHelper:
    @staticmethod
    def calculate_min(numbers: list[float]) ->Optional[float]:
        if numbers is None or len(numbers) == 0: return None
        return min(ArithmeticHelper.return_clean_numbers(numbers))

    @staticmethod
    def calculate_mean(numbers: list[float]) ->Optional[float]:
        if numbers is None or len(numbers) == 0: return None
        cleaned = ArithmeticHelper.return_clean_numbers(numbers)

        return sum(cleaned) / len(cleaned)

    @staticmethod
    def calculate_max(numbers: list[float]) ->Optional[float]:
        if numbers is None or len(numbers) == 0: return None
        return max(ArithmeticHelper.return_clean_numbers(numbers))

    @staticmethod
    def unique_items_count(items: list[str]) -> int:
        return len(set(items))

    @staticmethod
    def return_clean_numbers(numbers: list[Any]) -> list[float]:
        # Return a list of numbers, cleaning up any non-numeric values
        cleaned = []
        for num in numbers:
            try:
                parsed = float(num)
                cleaned.append(parsed)
            except (ValueError, TypeError):
                continue
        return cleaned

    @staticmethod
    def calculate_revenue_per_shipping_city(transactions: list[TransactionModel]) -> Dict[str, float]:
        revenue_dict = defaultdict(float)
        for txn in transactions:
            revenue = txn.discounted_price * txn.quantity
            revenue_dict[txn.shipping_city] += revenue
        return dict(revenue_dict)