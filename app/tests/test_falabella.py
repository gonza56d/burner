"""
Falabella tests.
"""

# App
from pages import FalabellaPage
from .with_fixtures import PyTest


class TestFalabellaPage(PyTest):
    """Falabella web page unit tests.
    """

    page = FalabellaPage()
