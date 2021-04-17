# Python
import unittest
# App
from app.pages import FalabellaPage


class TestFalabellaPage(unittest.TestCase):
    """
    Falabella web page unit tests.
    """

    def setUp(self) -> None:
        self.page = FalabellaPage()

    def test_get_categories(self) -> None:
        categories = self.page.get_categories()
        self.assertGreater(len(categories), 0, "No categories where found")
        for category in categories:
            self.assertIsNotNone(category.name, "Category didn't have a name")
            self.assertIsNotNone(category.href, "Category didn't have an href")

    def test_get_sales(self) -> None:
        sales = self.page.get_sales()
        self.assertGreater(len(sales), 0, "No sales where found")
        for sale in sales:
            self.assertIsNotNone(
                sale.product_id,
                "Sale didn't have an ID"
            )
            self.assertIsNotNone(
                sale.product_name,
                "Sale didn't have a product name"
            )
