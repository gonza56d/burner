"""
Project variable settings.
"""

# Python
import csv


# Selenium webdriver path
# Set the indicated driver for the execution environment
SELENIUM_DRIVER_PATH = './app/linux_chromedriver'

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
