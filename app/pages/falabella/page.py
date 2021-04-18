# Python
from datetime import date
from typing import List

# App
from .selenium_utils import FalabellaSeleniumUtils
from app.models import PageCategory
from app.pages import BasePage


class FalabellaPage(BasePage):
    """
    Page object model to collect data from Falabella web page.
    """

    PAGE_NAME = 'Falabella'
    CATEGORIES_STORAGE_FILENAME = 'falabella-categories'

    def get_categories(self) -> List[PageCategory]:
        """
        Get furniture categories from Falabella page.
        """

        categories = FalabellaSeleniumUtils().get_furnitures_categories()
        self.categories = []
        while True:
            try:
                category = next(categories)
                self.categories.append(
                    PageCategory(
                        page_name=FalabellaPage.PAGE_NAME,
                        category_name=category.text,
                        category_url=category.get_attribute('href'),
                        category_id=category.get_attribute('href').split('/')[5]
                    )
                )
            except StopIteration:
                break
        return self.categories

    @property
    def categories_storage_filename(self) -> str:
        _date = date.today()
        return f'{FalabellaPage.CATEGORIES_STORAGE_FILENAME}-{str(_date)}.csv'
