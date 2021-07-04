"""
Sodimac tests.
"""

# App
from pages import SodimacPage
from .with_fixtures import PyTest


class TestSodimacPage(PyTest):
    """Sodimac web page unit tests.
    """

    page = SodimacPage()
