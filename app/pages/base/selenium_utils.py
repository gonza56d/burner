# Python
from abc import ABC, abstractmethod

# Selenium
from selenium.webdriver import Chrome

# App
from settings import SELENIUM_DRIVER_PATH


class BaseSeleniumUtils(ABC):
    """Base abstract class for selenium classes.

    Implement Chromedriver and get to page url.
    """

    def __init__(self) -> None:
        """Constructor method.

        Set Chromedriver instance, maximize window and get to the page url
        to get ready for scraping.
        """
        self.driver = Chrome(executable_path=SELENIUM_DRIVER_PATH)
        self.driver.maximize_window()
        self.driver.get(self.get_page_url())

    @abstractmethod
    def get_page_url(self) -> str:
        """Get class attribute of page url.

        Return
        ------
        str : Page url.
        """
        pass
