from typing import List, Union
from datetime import date
from dateutil import relativedelta
from core.stock_list import TushareAPI
from core.equity import Equity
from strategy.strategy import Strategy
from fundamental.share_holder import ShareHolder


class ShareHolderStrategy(Strategy):
    def __init__(self):
        super().__init__()

    @staticmethod
    def find_share_holder_decrease(
            index_id: str, as_of_date: date = date.today()) -> List[str]:
        return_list = []
        index_components = TushareAPI.get_index_components(index_id)
        for stock_id in index_components:
            if stock_id[:3] in ['688', '900']:
                continue

            ShareHolder.get_count_history(Equity(stock_id))

    @staticmethod
    def is_share_count_decreasing(
            stock_id: Union[str, int, Equity],
            decrease_count: int,
            as_of_date: date = date.today()) -> bool:
        if isinstance(stock_id, Equity):
            count_history_list = ShareHolder.get_count_history(stock_id).to_dict("records")
        else:
            count_history_list = ShareHolder.get_count_history(Equity(stock_id)).to_dict("records")
        i = 0
        for i in range(len(count_history_list)):
            if count_history_list[i]["截止日期"] <= as_of_date:
                break

        for j in range(i, min(i+decrease_count, len(count_history_list) - 1)):
            if count_history_list[j]["股东户数"] >= count_history_list[j + 1]["股东户数"]:
                return False

        return True




