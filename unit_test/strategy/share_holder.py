import unittest
from datetime import date
from strategy.share_holder import ShareHolderStrategy


class MyTestCase(unittest.TestCase):
    def test_find_share_holder_decrease(self):
        self.assertEqual(True, ShareHolderStrategy.is_share_count_decreasing('300741', 3, date(2020, 12, 20)))
        self.assertEqual(False, ShareHolderStrategy.is_share_count_decreasing('002142', 3, date(2020, 12, 20)))
        self.assertEqual(True, ShareHolderStrategy.is_share_count_decreasing('002985', 3, date(2020, 12, 20)))
        self.assertEqual(False, ShareHolderStrategy.is_share_count_decreasing('603290', 3, date(2020, 12, 20)))


if __name__ == '__main__':
    unittest.main()
