"""
Sodimac tests.
"""

# Python
import os
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

    def tearDown(self) -> None:
        """Test case tear down. Delete files created during some test runs.

        Catch AttributeError exception and ignore it in case that the test ran
        didn't create any file (hence didn't set the filename attribute).
        """
        try:
            print('categories_filename:', self.categories_filename)
            os.remove(self.categories_filename)
        except AttributeError:
            pass
        try:
            print('products_filename:', self.products_filename)
            os.remove(self.products_filename)
        except AttributeError:
            pass
