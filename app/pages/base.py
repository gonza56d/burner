# Python
from abc import ABC, abstractmethod
from datetime import date

# App
from app.models import PageCategory
from app.settings import STORAGE_PATH, get_csv_writer


class BasePage(ABC):
    """
    Abstract class to implement how to get the data.
    
    It already implements how to store the data once it was collected.
    """

    @abstractmethod
    def get_categories(self):
        pass

    @property
    @abstractmethod
    def categories_storage_filename(self) -> str:
        pass

    def store_categories(self) -> None:
        """
        Store today's Page categories in CSV.

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
