"""
Classes with common tests cases to inherit in unittest.TestCase subclasses.
"""

# Python
from typing import Generator, List
from unittest.mock import MagicMock

# App
from .mocks import categories as category_mocks
from .mocks import products as product_mocks
from models import PageCategory


class CategoriesTestsMixin:
    """Common web pages categories data collection unit tests.

    Perform the following validations:
    * Categories from page with their attributes.
    * Categories from CSV with their attributes.
    """

    def test_get_categories(self) -> None:
        """Validate that categories are properly obtained.
        """
        self.page.get_categories = MagicMock(
            return_value=category_mocks.get_categories(self.page.PAGE_NAME)
        )
        page_categories = self.page.get_categories(key='value')
        self.validate_categories(page_categories)

    def test_store_categories(self) -> None:
        """Validate that categories are stored and read properly.
        """
        self.page.get_categories = MagicMock(
            return_value=category_mocks.get_categories(self.page.PAGE_NAME)
        )
        # Save a reference to created file in order to delete on test tear down
        self.categories_filename = self.page.store_categories()
        stored_categories = self.page.get_latest_categories()
        self.validate_categories(stored_categories)

    def validate_categories(self, categories: List[PageCategory]) -> None:
        """Ensure that categories have all the expected data.

        Parameters
        ----------
        categories : List[PageCategory]
            Categories to validate their data.
        """
        self.assertGreater(
            len(categories), 0, "No categories where found"
        )
        for category in categories:
            self.assertIsNotNone(category.page_name, "Category didn't have a page name")
            self.assertIsNotNone(category.category_name, "Category didn't have a name")
            self.assertIsNotNone(category.category_url, "Category didn't have a url")
            self.assertIsNotNone(category.category_id, "Category didn't have an ID")


class ProductsTestsMixin:
    """Common web pages products data collection unit tests.

    Perform the following validations:
    * Products from page with their attributes.
    * Products from CSV with their attributes.
    """

    def test_get_products(self) -> None:
        """Validate that products are properly obtained.
        """
        self.page.get_products = MagicMock(
            return_value=product_mocks.get_products(self.page.PAGE_NAME)
        )
        page_products = self.page.get_products(key='value')
        self.validate_products(page_products)

    def test_store_products(self) -> None:
        """Validate that products are stored and read properly.
        """
        self.page.get_products = MagicMock(
            return_value=product_mocks.get_products(self.page.PAGE_NAME)
        )
        # Save a reference to created file in order to delete on test tear down
        self.products_filename = self.page.store_products()
        stored_products = self.page.get_latest_products()
        self.validate_products(stored_products)

    def validate_products(self, products: Generator) -> None:
        """Ensure that products have all the expected data.

        Parameters
        ----------
        products : Generator
            Products to validate their data.
        """
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
