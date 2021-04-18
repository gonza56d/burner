# Selenium
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# App
from app.settings import SELENIUM_DRIVER_PATH


class FalabellaSeleniumUtils:
    """
    Falabella web page selenium utils.

    Utilities for scenarios where a browser is necessary to collect specific
    data. E.g. data that is lazy and won't be in DOM at the initial request.
    """

    PAGE_URL = 'https://www.falabella.com.ar/falabella-ar/'

    BY_CATEGORIES_BUTTON = (
        By.XPATH,
        '(*//div[@class="CategoryMenuButton-module_toggle-ref-container__21GmW"])[2]'
    )

    BY_FURNITURES_CATEGORY = (By.XPATH, '*//span[text()="Muebles"]')

    BY_FURNITURES_CATEGORIES = (
        By.XPATH,
        '*//li[@class="secondLevelMenu__title"]/a[contains(@href, '+
        '"/falabella-ar/category/") and not(contains(@href, "?"))]'
    )

    def __init__(self) -> None:
        self.driver = Chrome(executable_path=SELENIUM_DRIVER_PATH)
        self.driver.maximize_window()
        self.driver.get(FalabellaSeleniumUtils.PAGE_URL)

    @property
    def furnitures_category(self):
        categories_button = self.driver.find_element(
            *FalabellaSeleniumUtils.BY_CATEGORIES_BUTTON
        )
        categories_button.click()
        return self.driver.find_element(
            *FalabellaSeleniumUtils.BY_FURNITURES_CATEGORY
        )

    def hover_on_furnitures_category(self):
        hover = ActionChains(self.driver)\
            .move_to_element(self.furnitures_category)
        hover.perform()

    def get_furnitures_categories(self):
        self.hover_on_furnitures_category()
        furnitures_categories = self.driver.find_elements(
            *FalabellaSeleniumUtils.BY_FURNITURES_CATEGORIES
        )
        yield from furnitures_categories
