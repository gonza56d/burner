"""
Project variable settings.
"""

# Python
import csv
import platform


def get_selenium_driver_path():
    """
    Return either Linux or Mac chromedriver path regarding platform system.
    """
    if platform.system().lower() == 'darwin':
        return './app/mac_chromedriver'
    else:
        return './app/linux_chromedriver'


# Selenium webdriver path
# Set the indicated driver for the execution environment
SELENIUM_DRIVER_PATH = get_selenium_driver_path()

# Data storage (CSV files) path
STORAGE_PATH = './app/data/'

CATEGORIES_STORAGE_PATH = STORAGE_PATH + 'categories/'

PRODUCTS_STORAGE_PATH = STORAGE_PATH + 'products/'


def get_csv_writer(file):
    """
    Return app's CSV writer with the proper configurations.
    """
    return csv.writer(
        file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    )


def get_csv_reader(file):
    """
    Return app's CSV reader with the proper configurations.
    """
    return csv.reader(file, delimiter=',')
