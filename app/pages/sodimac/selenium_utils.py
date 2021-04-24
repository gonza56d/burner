"""
Sodimac Selenium utilities.
"""

# Python
from typing import Generator

# Selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# App
from pages import BaseSeleniumUtils


class SodimacSeleniumUtils(BaseSeleniumUtils):
    """Sodimac web page selenium utils.

    Utilities for scenarios where a browser is necessary to collect specific
    data. E.g. data that is lazy and won't be in DOM at the initial request.
    """

    PAGE_URL = 'https://www.sodimac.com.ar/sodimac-ar/'

    BY_ANNOYING_BUTTON = (
        By.XPATH,
        '*//button[@class="Location-module_cancel-button__1ApHm"]'
    )

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
    def annoying_button(self) -> WebElement:
        """Sometimes a notification is displayed randomly, preventing driver to
        click the desired category button.

        Returns
        -------
        WebElement : Notification button if appeared.
        """
        try:
            return self.driver.find_element(
                *SodimacSeleniumUtils.BY_ANNOYING_BUTTON
            )
        except NoSuchElementException:
            return None

    @property
    def furnitures_category(self) -> WebElement:
        """Close notification button if appeared and find furnitures category.

        Return
        ------
        WebElement : Furnitures category web element.
        """
        annoying_button = self.annoying_button
        if annoying_button is not None:
            annoying_button.click()
        return self.driver.find_element(
            *SodimacSeleniumUtils.BY_FURNITURES_CATEGORY
        )

    def get_furnitures_categories(self) -> Generator:
        """Click on furnitures category and find its nested sub categories.

        Return
        ------
        Generator : yield from categories found.
        """
        self.furnitures_category.click()
        furnitures_categories = self.driver.find_elements(
            *SodimacSeleniumUtils.BY_FURNITURES_CATEGORIES
        )
        yield from furnitures_categories
