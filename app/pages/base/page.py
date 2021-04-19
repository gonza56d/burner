# Python
from abc import ABC, abstractmethod


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
        Implement the name under which the CSV files are stored.
        """
        pass

    @property
    @abstractmethod
    def furnitures_categories(self):
        """
        Implement how to get furnitures categories from page.
        """
        pass
