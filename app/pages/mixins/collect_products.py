# Python
from datetime import date
from os import listdir
from os.path import isfile, join
from typing import List

# App
from app.models import PageCategory, PageProduct
from app.settings import (
    CATEGORIES_STORAGE_PATH,
    PRODUCTS_STORAGE_PATH,
    get_csv_reader,
    get_csv_writer
)


class CollectProductsMixin:
    """
    Mixin to inherit in page models that provides the possibility of
    collecting and storing products from the indicated page.
    """

    @staticmethod
    def get_dates_as_string(files: List[str], replace_lookup: str) -> List[str]:
        """
        Collect and return all the dates as string from the files' names.
        """
        str_dates = []
        for file in files:
            str_date = file.replace(
                replace_lookup + '-', ''
            ).replace('.csv', '')
            str_dates.append(str_date)
        return str_dates

    @staticmethod
    def get_str_dates_as_dates(str_dates: List[str]) -> List[date]:
        """
        Convert all the string dates to dates and return it.
        """
        dates = []
        for str_date in str_dates:
            _date = date(*[int(result) for result in str_date.split('-')])
            dates.append(_date)
        return dates

    @staticmethod
    def get_file_with_date(files: List[str], file_date: date) -> str:
        last_file = None
        for file in files:
            if str(file_date) in file:
                last_file = file
        return last_file

    def get_categories_files(self) -> str:
        """
        Find all the categories CSV files, then filter and return only
        those that have subclass' CATEGORIES_STORAGE_FILENAME in their filename.
        """
        all_categories_files = [
            f for f in listdir(CATEGORIES_STORAGE_PATH) 
            if isfile(join(CATEGORIES_STORAGE_PATH, f))
        ]
        categories_files = []
        for file in all_categories_files:
            if self.CATEGORIES_STORAGE_FILENAME in file:
                categories_files.append(file)
        return categories_files

    def get_latest_categories_file(self) -> str:
        """
        Get the CSV file with the latest date and subclass' 
        CATEGORIES_STORAGE_FILENAME in its filename.
        """
        files = self.get_categories_files()
        str_dates = self.get_dates_as_string(
            files,
            self.CATEGORIES_STORAGE_FILENAME
        )
        dates = self.get_str_dates_as_dates(str_dates)
        max_date = max(dates)
        last_categories_file = self.get_file_with_date(files, max_date)
        return last_categories_file

    def get_latest_categories(self) -> List[PageCategory]:
        categories = []
        last_categories_file = self.get_latest_categories_file()
        first = True  # avoid appending the CSV header (first row)
        with open(CATEGORIES_STORAGE_PATH + last_categories_file) as file:
            file = get_csv_reader(file)
            for row in file:
                if not first:
                    category = PageCategory(
                        page_name=row[0],
                        category_name=row[1],
                        category_url=row[2],
                        category_id=row[3]
                    )
                    categories.append(category)
                first = False
        return categories

    def get_products(self) -> List[PageProduct]:
        """
        Get products from furnitures category in a list of PageProduct models.
        """

        products = self.furnitures_products
        self.products = []
        while True:
            try:
                product = next(products)
                self.products.append(
                    PageProduct(
                        page_name=self.get_page_name(),
                        category_id=product.category_id,
                        product_id=product.product_id,
                        product_name=product.product_name,
                        product_price=product.product_price,
                    )
                )
            except StopIteration:
                break
        return self.products

    def store_products(self) -> None:
        """
        Store today's category products in CSV.

        HEADS UP! It will overwrite a file if it has the same name. Name are
        created with today's date.
        """

        print(f'Collecting and storing products from {self.__class__.__name__}...')

        with open(
            PRODUCTS_STORAGE_PATH + self.get_products_storage_filename(),
            mode='w'
        ) as file:

            file = get_csv_writer(file)
            file.writerow([header for header in PageProduct.CSV_HEADERS])
            for product in self.get_products():
                file.writerow([
                    self.get_page_name(),
                    product.category_id,
                    product.product_id,
                    product.product_name,
                    product.product_price,
                ])
