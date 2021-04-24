# Python
from datetime import date
from typing import Generator

# App
from pages import BasePage
from pages.mixins import CollectCategoriesMixin, CollectProductsMixin
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

    def get_products_in_page(self):
        return self.soup.find_all(
            'div',
            {'class': 'jsx-411745769 product ie11-product-container'}
        )

    @staticmethod
    def get_product_id_lookup(soup_product):
        return soup_product.find_all('a')[0]['href'].split('/')[5]

    @staticmethod
    def get_product_url_lookup(soup_product):
        return soup_product.find_all('a')[0]['href']

    @staticmethod
    def get_product_name_lookup(soup_product):
        return soup_product.find(
            'h2', {'class': 'jsx-411745769 product-title'}
        ).text

    @staticmethod
    def get_product_price_lookup(soup_product):
        fixed_price = soup_product.find(
            'div', {'class': 'jsx-4135487716 price jsx-175035124'}
        ).find_all('span')[0].text.replace('.', '').replace(',', '.').replace('$', '')
        return float(fixed_price)
