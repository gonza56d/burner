# Python
from typing import List

# App
from app.models import PageCategory


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
            self.assertIsNotNone(category.page_name, "Category didn't have page name")
            self.assertIsNotNone(category.category_name, "Category didn't have a name")
            self.assertIsNotNone(category.category_url, "Category didn't have a url")
            self.assertIsNotNone(category.category_id, "Category didn't have an ID")
