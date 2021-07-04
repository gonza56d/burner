"""
Classes with common tests cases with pytest implementation.
"""

# Python
from typing import List

# Pytest
import pytest

# App
from models import PageCategory


class CategoriesTestsMixin:
    """Common web pages categories data collection pytest implementation.

    Perform the following validations:
    * Categories from page with their attributes.
    * Categories from CSV with their attributes.
    """

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
