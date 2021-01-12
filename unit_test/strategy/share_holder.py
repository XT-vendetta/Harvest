import unittest
from datetime import date
from strategy.share_holder import ShareHolderDecreaseStrategy
from strategy.stock_filter import StockFilter


class MyTestCase(unittest.TestCase):
    def test_share_holder_decrease_strategy_evaluate(self):
        share_holder_decrease_strategy = ShareHolderDecreaseStrategy(3)
        self.assertEqual(True, share_holder_decrease_strategy.evaluate(date(2020, 12, 20), '300741'))
        self.assertEqual(False, share_holder_decrease_strategy.evaluate(date(2020, 12, 20), '002142'))
        self.assertEqual(True, share_holder_decrease_strategy.evaluate(date(2020, 12, 20), '002985'))
        self.assertEqual(False, share_holder_decrease_strategy.evaluate(date(2020, 12, 20), '603290'))

    def test_stock_filter(self):
        stock_ids = ['300741', '002142', '002985', '603290']
        share_holder_decrease_strategy = ShareHolderDecreaseStrategy(3)
        actual_results = StockFilter.apply_strategy_to_stock_list(
            date(2020, 12, 20),
            stock_ids,
            share_holder_decrease_strategy
        )
        target_results = [True, False, True, False]
        for i in range(4):
            self.assertEqual(target_results[i], actual_results[stock_ids[i]])


if __name__ == '__main__':
    unittest.main()
