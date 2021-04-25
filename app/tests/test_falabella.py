"""
Falabella tests.
"""

# Python
import os
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

    def tearDown(self) -> None:
        """Test case tear down. Delete files created during some test runs.

        Catch AttributeError exception and ignore it in case that the test ran
        didn't create any file (hence didn't set the filename attribute).
        """
        try:
            os.remove(self.categories_filename)
        except AttributeError:
            pass
        try:
            os.remove(self.products_filename)
        except AttributeError:
            pass
