# Python
from datetime import date
from typing import List

# App
from .selenium_utils import FalabellaSeleniumUtils
from app.models import PageCategory
from app.pages import BasePage


class FalabellaPage(BasePage):
    """
    Page object model that implements how to collect and store data
    from Falabella web page.
    """

    PAGE_NAME = 'Falabella'
    CATEGORIES_STORAGE_FILENAME = 'falabella-categories'

    def get_page_name(self):
        return self.PAGE_NAME

    def get_categories_storage_filename(self) -> str:
        _date = date.today()
        return f'{self.CATEGORIES_STORAGE_FILENAME}-{str(_date)}.csv'

    @property
    def furnitures_categories(self):
        return FalabellaSeleniumUtils().get_furnitures_categories()
