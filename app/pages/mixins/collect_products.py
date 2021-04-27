# Python
from datetime import date
from os import listdir
from os.path import isfile, join
import requests
from requests.exceptions import Timeout, RequestException
from typing import List, Generator

# BeautifulSoup
from bs4 import BeautifulSoup

# App
from models import PageCategory, PageProduct
from settings import (
    CATEGORIES_STORAGE_PATH,
    PRODUCTS_STORAGE_PATH,
    get_csv_reader,
    get_csv_writer
)


class CollectProductsMixin:
    """Mixin to inherit in page models.
    
    Provides the possibility of collecting and storing products from the
    subclass' indicated page.
    """

    @staticmethod
    def get_dates_as_string(files: List[str], replace_lookup: str) -> List[str]:
        """Collect and return all the dates as string from the files' names.

        Parameters
        ----------
        files : List[str]
            Collection to get the dates from.
        
        replace_lookup : str
            Part of the name in the files to remove together with file
            extension, leaving only the date in the filename.
        
        Return
        ------
        List[str] : Collection of the obtained dates.
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
        """Convert all the given string dates to Python date type.

        Parameters
        ----------
        str_dates : List[str]
            Collection of dates to convert.
        
        Return
        ------
        List[date] : Convertion results.
        """
        dates = []
        for str_date in str_dates:
            _date = date(*[int(result) for result in str_date.split('-')])
            dates.append(_date)
        return dates

    @staticmethod
    def get_file_with_date(files: List[str], file_date: date) -> str:
        """Filter a file in the list with the given date.

        Parameters
        ----------
        files : List[str]
            Collection of filenames to search from.

        file_date : date
            Date value to filter the file.
        
        Return
        ------
        str : First file match.
        None : No file with given date found.
        """
        last_file = None
        for file in files:
            if str(file_date) in file:
                last_file = file
                break
        return last_file

    def get_files(self, file_lookup: str, storage_path: str) -> List[str]:
        """Find and return CSV files filtering by file_lookup.

        Parameters
        ----------
        file_lookup : str
            Part of name to filter accepted files.
        
        storage_path : str
            Path where to find the desired files.
        
        Return
        ------
        List[str] : Result of filtered files.
        """
        all_categories_files = [
            f for f in listdir(storage_path) 
            if isfile(join(storage_path, f))
        ]
        categories_files = []
        for file in all_categories_files:
            if file_lookup in file:
                categories_files.append(file)
        return categories_files

    def get_latest_file(self, file_lookup: str, storage_path: str) -> str:
        """Get the CSV file with the latest date and file_lookup in its filename.

        Parameters
        ----------
        file_lookup : str
            Part of name to filter the files before comparing their dates.

        storage_path : str
            Path where to find the desired file.
        
        Return
        ------
        str : Filename of the file with the given name lookup and latest date.
        """
        files = self.get_files(file_lookup, storage_path)
        str_dates = self.get_dates_as_string(files, file_lookup)
        dates = self.get_str_dates_as_dates(str_dates)
        max_date = max(dates)
        last_categories_file = self.get_file_with_date(files, max_date)
        return last_categories_file

    def get_latest_products(self) -> Generator:
        """Get products from latest CSV file.

        Return
        ------
        Generator : yield from products in the CSV file.
        """
        products = []
        last_products_file = self.get_latest_file(
            self.PRODUCTS_STORAGE_FILENAME,
            PRODUCTS_STORAGE_PATH
        )
        first = True  # avoid appending the CSV header (first row)
        with open(PRODUCTS_STORAGE_PATH + last_products_file) as file:
            file = get_csv_reader(file)
            for row in file:
                if not first:
                    product = PageProduct(
                        page_name=row[0],
                        category_id=row[1],
                        product_id=row[2],
                        product_url=row[3],
                        product_name=row[4],
                        product_price=row[5],
                    )
                    products.append(product)
                first = False
        yield from products

    def get_latest_categories(self) -> List[PageCategory]:
        """Get categories from latest CSV file.

        Return
        ------
        List[PageCategory] : Categories in the CSV file.
        """
        categories = []
        last_categories_file = self.get_latest_file(
            self.CATEGORIES_STORAGE_FILENAME,
            CATEGORIES_STORAGE_PATH
        )
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
        """Get products from category page.

        Parameters
        ----------
        category : PageCategory
            Category page where to find products.

        Return
        ------
        Generator : yield from products found in the given category.
        """
        category_products = []
        try:
            request = requests.get(category.category_url, timeout=15)
            if request.status_code is not 200:
                raise RequestException
            self.soup = BeautifulSoup(request.text, 'html.parser')
            for page_product in self.get_products_in_page():
                product = PageProduct(
                    page_name=self.get_page_name(),
                    category_id=category.category_id,
                    product_id=self.get_product_id_lookup(page_product),
                    product_url=self.get_product_url_lookup(page_product),
                    product_name=self.get_product_name_lookup(page_product),
                    product_price=self.get_product_price_lookup(page_product)
                )
                category_products.append(product)
        except Timeout:
            print(f' * Timeout: Get request for {category.category_url} timed out after 15 seconds.')
        except RequestException:
            print(f' * RequestException: Response code for request {category.category_url} was {request.status_code}')
        finally:
            yield from category_products

    def get_products(self) -> Generator:
        """Get products from furnitures category in a generator of PageProduct
        objects.

        Return
        ------
        Generator : yield from products found.
        """

        products = self.furnitures_products

        # mauricio: Here we are doing an expensive work, using list iteration and not
        # taking advantage of the generator.
        self.products = []
        while True:
            try:
                product = next(products)
                self.products.append(
                    PageProduct(
                        page_name=self.get_page_name(),
                        category_id=product.category_id,
                        product_id=product.product_id,
                        product_url=product.product_url,
                        product_name=product.product_name,
                        product_price=product.product_price,
                    )
                )
            except StopIteration:
                break
        yield from self.products

    def store_products(self) -> str:
        """Store today's category products in CSV.

        HEADS UP! It will overwrite a file if it has the same name. Name are
        created with today's date.

        Return
        ------
        str : Filename of the created CSV with the products.
        """

        print(f'Collecting and storing products from {self.__class__.__name__}...')

        filename = PRODUCTS_STORAGE_PATH + self.get_products_storage_filename()

        with open(filename, mode='w') as file:

            file = get_csv_writer(file)
            file.writerow([header for header in PageProduct.CSV_HEADERS])
            products = self.get_products()
            while True:
                try:
                    product = next(products)
                    file.writerow([
                        self.get_page_name(),
                        product.category_id,
                        product.product_id,
                        product.product_url,
                        product.product_name,
                        product.product_price,
                    ])
                except StopIteration:
                    break

        print(f'Finished products from {self.__class__.__name__}.')
        return filename
