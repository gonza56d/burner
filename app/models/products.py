
class PageProduct:
    """
    Model to store web page product data.
    """

    CSV_HEADERS = [
        'STORE_NAME', 'CATEGORY_ID', 'PRODUCT_ID', 'PRODUCT_NAME', 'PRODUCT_PRICE'
    ]

    def __init__(self, page_name: str, category_id: str, product_id: str,
                 product_url: str, product_name: str, product_price: float) -> None:

        self.page_name = page_name
        self.category_id = category_id
        self.product_id = product_id.strip()
        self.product_url = product_url.strip()
        self.product_name = product_name.strip()
        self.product_price = product_price
