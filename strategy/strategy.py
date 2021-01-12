from typing import Union
from datetime import date
from core.equity import Equity


class Strategy:
    def __init__(self):
        pass

    def evaluate(self, evaluate_date: date = date.today(), stock_id: Union[str, int, Equity] = None):
        raise NotImplementedError("Method evaluate of base class Strategy is not supported.")
