# Python
from typing import List

# App
from app.models import PageCategory
from app.settings import STORAGE_PATH, get_csv_writer


class CollectCategoriesMixin:
    """
    Mixin to inherit in page models that provides the possibility of
    collecting and storing categories from the indicated page.
    """

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
                        category_name=category.text.replace(' >', ''),
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

        print(f'Collecting and storing categories from {self.__class__.__name__}...')

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
