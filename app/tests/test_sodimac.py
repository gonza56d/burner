"""
Sodimac tests.
"""

# Python
import os
# from unittest import TestCase

# App
from pages import SodimacPage
from .with_fixtures import CategoriesTestsMixin


class TestSodimacPage(CategoriesTestsMixin):
    """Sodimac web page unit tests.
    """

    page = SodimacPage()
