# Python
from typing import List

# App
from .selenium_utils import FalabellaSeleniumUtils
from app.models import PageCategory


class FalabellaPage:
    """
    Page object model to collect data from Falabella web page.
    """
    
    PAGE_NAME = 'Falabella'

    def get_categories(self) -> List[PageCategory]:
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
