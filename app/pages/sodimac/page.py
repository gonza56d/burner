# Python
from datetime import date
from typing import Generator

# App
from app.pages import BasePage
from app.pages.mixins import CollectCategoriesMixin, CollectProductsMixin
from .selenium_utils import SodimacSeleniumUtils


class SodimacPage(
        BasePage,
        CollectCategoriesMixin,
        CollectProductsMixin
    ):
    """
    Page model that to collect and store data from Sodimac web page.
    """

    PAGE_NAME = 'Sodimac'
    CATEGORIES_STORAGE_FILENAME = 'sodimac-categories'
    PRODUCTS_STORAGE_FILENAME = 'sodimac-products'

    def get_page_name(self) -> str:
        return self.PAGE_NAME

    def get_categories_storage_filename(self) -> str:
        _date = date.today()
        return f'{self.CATEGORIES_STORAGE_FILENAME}-{str(_date)}.csv'

    def get_products_storage_filename(self) -> str:
        _date = date.today()
        return f'{self.PRODUCTS_STORAGE_FILENAME}-{str(_date)}.csv'

    @property
    def furnitures_categories(self) -> Generator:
        return SodimacSeleniumUtils().get_furnitures_categories()

    @property
    def furnitures_products(self) -> Generator:
        pass # TODO 
