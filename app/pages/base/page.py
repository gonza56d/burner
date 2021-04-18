# Python
from abc import ABC, abstractmethod
from typing import List

# App
from app.models import PageCategory
from app.settings import STORAGE_PATH, get_csv_writer


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

    def get_categories(self) -> List[PageCategory]:
        """
        Get nested categories from furnitures categories in a list of
        PageCategory models.
        """

        categories = self.furnitures_categories
        self.categories = []
        while True:
            try:
                category = next(categories)
                self.categories.append(
                    PageCategory(
                        page_name=self.get_page_name(),
                        category_name=category.text,
                        category_url=category.get_attribute('href'),
                        category_id=category.get_attribute('href').split('/')[5]
                    )
                )
            except StopIteration:
                break
        return self.categories

    def store_categories(self) -> None:
        """
        Store today's Page categories in CSV.

        HEADS UP! It will overwrite a file if it has the same name. Name are
        created with today's date.
        """

        with open(
            STORAGE_PATH + self.get_categories_storage_filename(), mode='w'
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
