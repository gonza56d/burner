# Python
from datetime import date
from typing import List

# App
from .selenium_utils import FalabellaSeleniumUtils
from app.models import PageCategory
from app.settings import STORAGE_PATH, get_csv_writer


class FalabellaPage:
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

    def store_categories(self) -> None:
        """
        Store today's Falabella categories in CSV.

        HEADS UP! It will overwrite a file if it has the same name. Name are
        created with today's date.
        """

        with open(
            STORAGE_PATH + self.categories_storage_filename, mode='w'
        ) as file:

            file = get_csv_writer(file)
            file.writerow([header for header in PageCategory.CSV_HEADERS])
            for category in self.get_categories():
                file.writerow([
                    category.page_name,
                    category.category_name,
                    category.category_url,
                    category.category_id
                ])
