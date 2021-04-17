# Python
import unittest
# App
from app.pages import FalabellaPage


class TestFalabellaPage(unittest.TestCase):
    """
    Falabella web page unit tests.
    """

    def setUp(self) -> None:
        self.page = FalabellaPage()
