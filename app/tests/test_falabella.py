"""
Falabella tests.
"""

# Python
from unittest import TestCase

# App
from pages import FalabellaPage
from .common import CommonTestsMixin


class TestFalabellaPage(TestCase, CommonTestsMixin):
    """Falabella web page unit tests.
    """

    def setUp(self) -> None:
        """Test case set up. Indicate page attribute to run tests.
        """
        self.page = FalabellaPage()
