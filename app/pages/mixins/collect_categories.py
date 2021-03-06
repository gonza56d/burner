# Python
from typing import List

# App
from models import PageCategory
from settings import CATEGORIES_STORAGE_PATH, get_csv_writer


class CollectCategoriesMixin:
    """Mixin to inherit in page models.
    
    Provides the possibility of collecting and storing categories from the
    subclass' indicated page.
    """

    def get_categories(self) -> List[PageCategory]:
        """Get nested categories from furnitures categories.

        Return
        ------
        List[PageCategory] : Categories found.
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

    def store_categories(self) -> str:
        """Store today's page categories in CSV.

        HEADS UP! It will overwrite a file if it has the same name. Name are
        created with today's date.

        Return
        ------
        str : Filename of the created CSV with the categories.
        """

        print(f'Collecting and storing categories from {self.__class__.__name__}...')

        filename = CATEGORIES_STORAGE_PATH + self.get_categories_storage_filename()

        with open(filename, mode='w') as file:

            file = get_csv_writer(file)
            file.writerow([header for header in PageCategory.CSV_HEADERS])
            for category in self.get_categories():
                file.writerow([
                    category.page_name,
                    category.category_name,
                    category.category_url,
                    category.category_id
                ])

        print(f'Finished categories from {self.__class__.__name__}.')
        return filename
