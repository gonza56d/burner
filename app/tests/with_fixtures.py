"""
Classes with common tests cases with pytest implementation.
"""

# Python
from typing import Generator, List

# Pytest
import pytest

# App
from models import PageCategory, PageProduct


class PyTest:
    """Common web pages data collection pytest implementation.

    Perform the following validations:
    * Categories from page with their attributes.
    * Categories from CSV with their attributes.
    """

    @pytest.fixture
    def products(self) -> List[PageProduct]:
        return [
            PageProduct(self.page.PAGE_NAME, 'tables', 'tbl_black', 'www.fake.com', 'black table', 1305.30),
            PageProduct(self.page.PAGE_NAME, 'chairs', 'cha_black', 'www.fake.com', 'black chair', 305.30),
            PageProduct(self.page.PAGE_NAME, 'desks', 'dsk_black', 'www.fake.com', 'black desk', 1996.00),
        ]

    @pytest.fixture
    def categories(self) -> List[PageCategory]:
        return [
            PageCategory(self.page.PAGE_NAME, 'tables', 'www.fake.com', 'tables'),
            PageCategory(self.page.PAGE_NAME, 'chairs', 'www.fake.com', 'chairs'),
            PageCategory(self.page.PAGE_NAME, 'desks', 'www.fake.com', 'desks'),
        ]

    def test_get_categories(self, categories) -> None:
        self.validate_categories(categories)

    def test_store_categories(self, categories) -> None:
        """Validate that categories are stored and read properly.
        """
        self.page.get_categories = lambda: categories
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
        assert len(categories) > 0
        for category in categories:
            assert category.page_name
            assert category.category_name
            assert category.category_url
            assert category.category_id

    def test_store_products(self, products) -> None:
        self.page.get_category_products = yield from products
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
                assert product.page_name
                assert product.category_id
                assert product.product_id
                assert product.product_url
                assert product.product_name
                assert product.product_price is not None
            except StopIteration:
                break
        assert count > 0
