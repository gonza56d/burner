
class PageCategory:
    """
    Model to store web page category data.
    """

    CSV_HEADERS = ['STORE_NAME', 'CATEGORY_NAME', 'CATEGORY_URL', 'CATEGORY_ID']

    def __init__(self, page_name: str, category_name: str,
                 category_url: str, category_id: str) -> None:

        self.page_name = page_name
        self.category_name = category_name.strip()
        self.category_url = category_url.strip()
        self.category_id = category_id.strip()
