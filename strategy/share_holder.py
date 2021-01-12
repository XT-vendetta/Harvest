from typing import Union
from datetime import date
from core.equity import Equity
from strategy.strategy import Strategy
from fundamental.share_holder import ShareHolder


class ShareHolderDecreaseStrategy(Strategy):
    def __init__(self, decrease_count: int = 3):
        super().__init__()
        self.decrease_count = decrease_count

    def evaluate(self, evaluate_date: date = date.today(), stock_id: Union[str, int, Equity] = None) -> bool:
        if stock_id is None:
            raise RuntimeError("Cannot evaluate with stock_id being None.")
        elif isinstance(stock_id, Equity):
            count_history_list = ShareHolder.get_count_history(stock_id).to_dict("records")
        else:
            count_history_list = ShareHolder.get_count_history(Equity(stock_id)).to_dict("records")
        i = 0
        for i in range(len(count_history_list)):
            if count_history_list[i]["截止日期"] <= evaluate_date:
                break

        for j in range(i, min(i + self.decrease_count, len(count_history_list) - 1)):
            if count_history_list[j]["股东户数"] >= count_history_list[j + 1]["股东户数"]:
                return False

        return True




