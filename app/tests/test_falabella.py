# Python
from unittest import TestCase

# App
from pages import FalabellaPage
from .common import CommonTestsMixin


class TestFalabellaPage(TestCase, CommonTestsMixin):
    """
    Falabella web page unit tests.
    """

    def setUp(self) -> None:
        self.page = FalabellaPage()
