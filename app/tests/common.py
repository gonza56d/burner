# Python
from typing import List


class CommonTestsMixin:
    """
    Common web pages data collection unit tests.

    Perform the following validations:
    * Categories from page with their ID, name and href.
    * Sales from any category, with their ID, name, category ID and price.
    * Sales from CSV result file, with their ID, name, category ID and price. 
    """

    def test_get_categories(self) -> None:
        page_categories = self.page.get_categories()
        self.assertGreater(len(page_categories), 0, "No categories where found")
        for category in page_categories:
            self.assertIsNotNone(category.id, "Category didn't have an id")
            self.assertIsNotNone(category.name, "Category didn't have a name")
            self.assertIsNotNone(category.href, "Category didn't have an href")

    def test_get_sales(self) -> None:
        page_sales = self.page.get_sales()
        self.validate_sales(page_sales)

    def test_csv_results(self) -> None:
        csv_results = self.page.get_result_csv()  # TODO must return a list of Sale objects
        self.validate_sales(csv_results)

    def validate_sales(self, sales: List) -> None:
        """
        Validate common Sale objects collected data.
        """

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
            self.assertIsNotNone(
                sale.product_category_id,
                "Sale didn't have a product category ID"
            )
            self.assertIsNotNone(
                sale.product_price,
                "Sale didn't have a product price"
            )
