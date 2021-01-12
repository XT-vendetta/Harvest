from typing import List, Dict
from datetime import date
from strategy.strategy import Strategy
from core.stock_list import TushareAPI


class StockFilter:
    def __init__(self):
        pass

    @staticmethod
    def apply_strategy_to_stock_list(evaluate_date: date, stock_ids: List[str], strategy: Strategy) -> Dict[str, bool]:
        return {stock_id: strategy.evaluate(evaluate_date, stock_id) for stock_id in stock_ids}

    @staticmethod
    def apply_strategy_to_index(evaluate_date: date, index_id: str, strategy: Strategy) -> Dict[str, bool]:
        index_components = TushareAPI.get_index_components(index_id)
        return StockFilter.apply_strategy_to_stock_list(evaluate_date, index_components, strategy)