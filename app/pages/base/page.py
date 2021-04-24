# Python
from abc import ABC, abstractmethod
from typing import Generator


class BasePage(ABC):
    """Abstract class that implements how to get and store the data regarding
    subclass attributes.
    """

    @abstractmethod
    def get_page_name(self) -> str:
        """Implement the name of the page to store results from.

        Return
        ------
        str : Name of the page.
        """
        pass

    @abstractmethod
    def get_categories_storage_filename(self) -> str:
        """Implement the name under which the categories CSV files are stored.

        Return
        ------
        str : Filename for categories CSVs.
        """
        pass

    @abstractmethod
    def get_products_storage_filename(self) -> str:
        """Implement the name under which the products CSV files are stored.

        Return
        ------
        str : Filename for products CSVs.
        """
        pass

    @property
    @abstractmethod
    def furnitures_categories(self) -> Generator:
        """Implement how to get furnitures categories from page.

        Return
        ------
        Generator : yield from furnitures found.
        """
        pass

    @abstractmethod
    def get_product_id_lookup(soup_product) -> str:
        """Implement lookup to find product id.

        Return
        ------
        str : ID of the given BS4 product.
        """
        pass

    @abstractmethod
    def get_product_url_lookup(soup_product) -> str:
        """Implement lookup to find product url.

        Return
        ------
        str : URL of the given BS4 product.
        """
        pass

    @abstractmethod
    def get_product_name_lookup(soup_product) -> str:
        """Implement lookup to find product name.

        Return
        ------
        str : Name of the given BS4 product.
        """
        pass

    @abstractmethod
    def get_product_price_lookup(soup_product) -> float:
        """Implement lookup to find product price.

        Return
        ------
        float : Price of the given BS4 product.
        """
        pass
