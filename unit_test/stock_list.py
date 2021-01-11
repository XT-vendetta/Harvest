import unittest
from core.stock_list import TushareAPI


class MyTestCase(unittest.TestCase):
    def test_get_from_web(self):
        a = TushareAPI.get_from_web()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
