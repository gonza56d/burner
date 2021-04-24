"""
Sodimac tests.
"""

# Python
from unittest import TestCase

# App
from pages import SodimacPage
from .common import CategoriesTestsMixin, ProductsTestsMixin


class TestSodimacPage(TestCase, CategoriesTestsMixin, ProductsTestsMixin):
    """Sodimac web page unit tests.
    """

    def setUp(self) -> None:
        """Test case set up. Indicate page attribute to run tests.
        """
        self.page = SodimacPage()
