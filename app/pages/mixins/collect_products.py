# Python
from typing import List

# App
from app.models import PageProduct
from app.settings import STORAGE_PATH, get_csv_writer


class CollectProductsMixin:
    """
    Mixin to inherit in page models that provides the possibility of
    collecting and storing products from the indicated page.
    """

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
                        category_id=category_id,
                        product_id=product_id,
                        product_name=product_name,
                        product_price=product_price,
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
            STORAGE_PATH + self.get_products_storage_filename(), mode='w'
        ) as file:

            file = get_csv_writer(file)
            file.writerow([header for header in PageProduct.CSV_HEADERS])
            for category in self.get_products():
                file.writerow([
                    category.page_name,
                    category.category_id,
                    category.product_id,
                    category.product_name,
                    category.product_price
                ])
