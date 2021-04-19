# Python
from abc import ABC, abstractmethod
from typing import Generator


class BasePage(ABC):
    """
    Abstract class that implements how to get and store the data regarding
    subclass attributes.
    """

    @abstractmethod
    def get_page_name(self) -> str:
        """
        Implement the name of the page to store.
        """
        pass

    @abstractmethod
    def get_categories_storage_filename(self) -> str:
        """
        Implement the name under which the categories CSV files are stored.
        """
        pass

    @abstractmethod
    def get_products_storage_filename(self) -> str:
        """
        Implement the name under which the products CSV files are stored.
        """
        pass

    @property
    @abstractmethod
    def furnitures_categories(self) -> Generator:
        """
        Implement how to get furnitures categories from page.
        """
        pass

    @abstractmethod
    def get_product_id_lookup(soup_product):
        """
        Implement lookup to find product id in the page.
        """
        pass

    @abstractmethod
    def get_product_url_lookup(soup_product):
        """
        Implement lookup to find product url in the page.
        """
        pass

    @abstractmethod
    def get_product_name_lookup(soup_product):
        """
        Implement lookup to find product name in the page.
        """
        pass

    @abstractmethod
    def get_product_price_lookup(soup_product):
        """
        Implement lookup to find product price in the page.
        """
        pass
