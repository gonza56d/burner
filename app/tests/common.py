# Python
from typing import Generator, List

# App
from app.models import PageCategory, PageProduct


class CommonTestsMixin:
    """
    Common web pages data collection unit tests.

    Perform the following validations:
    * Categories from page with their attributes.
    * Categories from CSV with their attributes.
    * Products from page with their attributes.
    * Products from CSV with their attributes.
    """

    def test_get_categories(self) -> None:
        page_categories = self.page.get_categories()
        self.validate_categories(page_categories)

    def test_store_categories(self) -> None:
        self.page.store_categories()
        stored_categories = self.page.get_latest_categories()
        self.validate_categories(stored_categories)

    def validate_categories(self, categories: List[PageCategory]) -> None:
        self.assertGreater(
            len(categories), 0, "No categories where found"
        )
        for category in categories:
            self.assertIsNotNone(category.page_name, "Category didn't have a page name")
            self.assertIsNotNone(category.category_name, "Category didn't have a name")
            self.assertIsNotNone(category.category_url, "Category didn't have a url")
            self.assertIsNotNone(category.category_id, "Category didn't have an ID")

    def test_get_products(self) -> None:
        page_products = self.page.get_products()
        self.validate_products(page_products)

    def test_store_products(self) -> None:
        self.page.store_products()
        stored_products = self.page.get_latest_products()
        self.validate_products(stored_products)

    def validate_products(self, products: Generator) -> None:
        count = 0
        while True:
            try:
                product = next(products)
                count += 1
                self.assertIsNotNone(product.page_name, "product didn't have a page name")
                self.assertIsNotNone(product.category_id, "product didn't have a category id")
                self.assertIsNotNone(product.product_id, "product didn't have a product id")
                self.assertIsNotNone(product.product_url, "product didn't have a product url")
                self.assertIsNotNone(product.product_name, "product didn't have a product name")
                self.assertIsNotNone(product.product_price, "product didn't have a product price")
            except StopIteration:
                break
        self.assertGreater(count, 0, "No products where found")
