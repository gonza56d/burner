"""
Falabella Selenium utilities.
"""

# Python
from typing import Generator

# Selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# App
from pages import BaseSeleniumUtils


class FalabellaSeleniumUtils(BaseSeleniumUtils):
    """Falabella web page selenium utils.

    Utilities for scenarios where a browser is necessary to collect specific
    data. E.g. data that is lazy and won't be in DOM at the initial request.
    """

    PAGE_URL = 'https://www.falabella.com.ar/falabella-ar/'

    BY_CATEGORIES_BUTTON = (
        By.XPATH,
        '(*//div[@class="CategoryMenuButton-module_toggle-' +
        'ref-container__21GmW"])[2]'
    )

    BY_FURNITURES_CATEGORY = (By.XPATH, '*//span[text()="Deco hogar"]')

    BY_FURNITURES_CATEGORIES = (
        By.XPATH,
        '*//li[@class="secondLevelMenu__title"]/a[contains(@href, ' +
        '"/falabella-ar/category/") and not(contains(@href, "?"))]'
    )

    def get_page_url(self):
        return self.PAGE_URL

    @property
    def furnitures_category(self) -> WebElement:
        """Click on furnitures category and return its nested subcategories
        in the page.

        Return
        ------
        WebElement : Furnitures category web element.
        """
        categories_button = self.driver.find_element(
            *FalabellaSeleniumUtils.BY_CATEGORIES_BUTTON
        )
        categories_button.click()
        return self.driver.find_element(
            *FalabellaSeleniumUtils.BY_FURNITURES_CATEGORY
        )

    def hover_on_furnitures_category(self) -> None:
        """Hover on furnitures category in order to display its
        nested categories.
        """
        hover = ActionChains(self.driver)\
            .move_to_element(self.furnitures_category)
        hover.perform()

    def get_furnitures_categories(self) -> Generator:
        """Find furnitures nested categories web elements.

        Return
        ------
        Generator : yield from furnitures categories found.
        """
        self.hover_on_furnitures_category()
        furnitures_categories = self.driver.find_elements(
            *FalabellaSeleniumUtils.BY_FURNITURES_CATEGORIES
        )
        yield from furnitures_categories
