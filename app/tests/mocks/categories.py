"""Page categories mocks."""

# Python
from typing import List

# App
from models import PageCategory


def get_categories(page_name: str) -> List[PageCategory]:
    """Get mocked categories to run unit tests.

    Parameters
    ----------
    page_name : str
        Name of the page to set as attribute in the mocked categories.
    
    Return
    ------
    List[PageCategory] : Mocked categories for unit testing.
    """
    return [
        PageCategory(page_name, 'tables', 'www.fake.com', 'tables'),
        PageCategory(page_name, 'chairs', 'www.fake.com', 'chairs'),
        PageCategory(page_name, 'desks', 'www.fake.com', 'desks'),
    ]
