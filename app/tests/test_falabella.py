"""
Falabella tests.
"""

# Python
from unittest import TestCase

# App
from pages import FalabellaPage
from .common import CategoriesTestsMixin, ProductsTestsMixin


class TestFalabellaPage(TestCase, CategoriesTestsMixin, ProductsTestsMixin):
    """Falabella web page unit tests.
    """

    def setUp(self) -> None:
        """Test case set up. Indicate page attribute to run tests.
        """
        self.page = FalabellaPage()
