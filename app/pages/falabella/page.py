# Python
from datetime import date
from typing import Generator

# App
from app.pages import BasePage
from app.pages.mixins import CollectCategoriesMixin, CollectProductsMixin
from .selenium_utils import FalabellaSeleniumUtils


class FalabellaPage(
        BasePage,
        CollectCategoriesMixin,
        CollectProductsMixin
    ):
    """
    Page model that to collect and store data from Falabella web page.
    """

    PAGE_NAME = 'Falabella'
    CATEGORIES_STORAGE_FILENAME = 'falabella-categories'
    PRODUCTS_STORAGE_FILENAME = 'falabella-products'

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
        return FalabellaSeleniumUtils().get_furnitures_categories()

    def get_products_in_page(self):
        return self.soup.find_all(
            'div',
            {'class': 'jsx-3488318063 jsx-3886284353 pod pod-4_GRID'}
        )

    @staticmethod
    def get_product_id_lookup(soup_product):
        return soup_product.find_all('a')[0]['href'].split('/')[5]

    @staticmethod
    def get_product_url_lookup(soup_product):
        return soup_product.find_all('a')[0]['href']

    @staticmethod
    def get_product_name_lookup(soup_product):
        return soup_product.find('b', {'class': 'pod-subTitle'}).text

    @staticmethod
    def get_product_price_lookup(soup_product):
        fixed_price = soup_product.find('li', {'class': 'price-0'})\
            ['data-undefined-price'].replace('.', '').replace(',', '.')
        return float(fixed_price)
