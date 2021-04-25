"""Page products mocks."""

# Python
from typing import Generator

# App
from models import PageProduct


def get_products(page_name: str) -> Generator:
    """Get mocked products to run unit tests.

    Parameters
    ----------
    page_name : str
        Name of the page to set as attribute in the mocked products.
    
    Return
    ------
    Generator : Yield from mocked products for unit testing.
    """
    yield from [
        PageProduct(
            page_name,
            'tables',
            'tbl_black',
            'www.fake.com',
            'black table',
            1305.30,
        ),
        PageProduct(
            page_name,
            'chairs',
            'cha_black',
            'www.fake.com',
            'black chair',
            305.30,
        ),
        PageProduct(
            page_name,
            'desks',
            'dsk_black',
            'www.fake.com',
            'black desk',
            1996.00,
        ),
    ]
