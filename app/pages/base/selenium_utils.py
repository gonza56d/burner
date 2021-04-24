# Python
from abc import ABC, abstractmethod

# Selenium
from selenium.webdriver import Chrome

# App
from settings import SELENIUM_DRIVER_PATH


class BaseSeleniumUtils(ABC):

    def __init__(self) -> None:
        self.driver = Chrome(executable_path=SELENIUM_DRIVER_PATH)
        self.driver.maximize_window()
        self.driver.get(self.get_page_url())

    @abstractmethod
    def get_page_url(self):
        pass
