"""Page categories mocks."""

# Python
from typing import List

# App
from models import PageCategory


def get_categories(page_name: str) -> List[PageCategory]:
    return [
        PageCategory(page_name, 'tables', 'www.fake.com', 'tables'),
        PageCategory(page_name, 'chairs', 'www.fake.com', 'chairs'),
        PageCategory(page_name, 'desks', 'www.fake.com', 'desks'),
    ]
