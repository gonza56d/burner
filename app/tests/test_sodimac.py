# Python
from unittest import TestCase

# App
from app.pages import SodimacPage
from .common import CommonTestsMixin


class TestSodimacPage(TestCase, CommonTestsMixin):
    """
    Sodimac web page unit tests.
    """

    def setUp(self) -> None:
        self.page = SodimacPage()
