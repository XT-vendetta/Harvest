from datetime import date
from core.stock_list import TushareAPI
from strategy.share_holder import ShareHolderDecreaseStrategy
from strategy.stock_filter import StockFilter


if __name__ == '__main__':
    stock_list = TushareAPI.get_index_components('000001')
    stock_list = [stock for stock in stock_list if stock[:3] not in ['900', '688']]
    share_holder_decrease_strategy = ShareHolderDecreaseStrategy(3)
    r = StockFilter.apply_strategy_to_stock_list(date(2020, 12, 30), stock_list[:100], share_holder_decrease_strategy)
    for k, v in r.items():
        if v is True:
            print(k)