# Python
from typing import Generator

# Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# App
from app.pages import BaseSeleniumUtils


class SodimacSeleniumUtils(BaseSeleniumUtils):
    """
    Sodimac web page selenium utils.

    Utilities for scenarios where a browser is necessary to collect specific
    data. E.g. data that is lazy and won't be in DOM at the initial request.
    """

    PAGE_URL = 'https://www.sodimac.com.ar/sodimac-ar/'

    BY_FURNITURES_CATEGORY = (
        By.XPATH,
        '*//a[text()="Muebles y Organización"]'
    )

    BY_FURNITURES_CATEGORIES = (
        By.XPATH,
        '*//ul[@class="menu-list-desktop"]/li[contains(@class, "link-primary' +
        '")]/a[contains(@href, "https://www.sodimac.com.ar/sodimac-ar/")]'
    )

    def get_page_url(self):
        return self.PAGE_URL

    @property
    def furnitures_category(self) -> WebElement:
        return self.driver.find_element(
            *SodimacSeleniumUtils.BY_FURNITURES_CATEGORY
        )

    def get_furnitures_categories(self) -> Generator:
        self.furnitures_category.click()
        furnitures_categories = self.driver.find_elements(
            *SodimacSeleniumUtils.BY_FURNITURES_CATEGORIES
        )
        yield from furnitures_categories
