"""
Falabella tests.
"""

# Python
import os
# from unittest import TestCase

# App
from pages import FalabellaPage
from .with_fixtures import CategoriesTestsMixin


class TestFalabellaPage(CategoriesTestsMixin):
    """Falabella web page unit tests.
    """

    page = FalabellaPage()
