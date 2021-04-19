# Python
from datetime import date
import requests
from typing import Generator

# BeautifulSoup
from bs4 import BeautifulSoup

# App
from app.models import PageCategory, PageProduct
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

    @property
    def furnitures_products(self) -> Generator:
        products = []
        for category in self.get_latest_categories():
            _category_products = self.get_category_products(category)
            while True:
                try:
                    category_product = next(_category_products)
                    products.append(category_product)
                except StopIteration:
                    break
        yield from products

    def get_category_products(self, category: PageCategory) -> Generator:
        category_products = []
        request = requests.get(category.category_url)
        soup = BeautifulSoup(request.text, 'html.parser')
        product_divs = soup.find_all(
            'div',
            {'class': 'jsx-3488318063 jsx-3886284353 pod pod-4_GRID'}
        )
        for product_div in product_divs:
            page_product = PageProduct(
                page_name=FalabellaPage.PAGE_NAME,
                category_id=category.category_id,
                product_id=product_div.find_all('a')[0]['href'].split('/')[5],
                product_url=product_div.find_all('a')[0]['href'],
                product_name=product_div.find('b', {'class': 'pod-subTitle'}).text,
                product_price=product_div.find('li', {'class': 'price-0'})['data-undefined-price']
            )
            category_products.append(page_product)
        yield from category_products
