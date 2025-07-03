# test_Shopping_list.py
import unittest
from ttest.temp.study import ShoppingList


class TestShoppingList(unittest.TestCase):
    def setUp(self):  # ✅ 拼写必须正确
        self.shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "牙膏": 15})

    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 55)


if __name__ == "__main__":
    unittest.main()
