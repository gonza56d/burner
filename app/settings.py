"""
Project variable settings.
"""

# Python
import csv
from io import TextIOWrapper
import platform


def get_selenium_driver_path() -> str:
    """Return either Linux or Mac chromedriver path regarding platform system.

    Return
    ------
    str : Path to the Selenium Chromedriver for the platform system.
    """
    if platform.system().lower() == 'darwin':
        return './mac_chromedriver'
    else:
        return './linux_chromedriver'


# Selenium webdriver path
# Set the indicated driver for the execution environment
SELENIUM_DRIVER_PATH = get_selenium_driver_path()

# Data storage (CSV files) path
STORAGE_PATH = './data/'

CATEGORIES_STORAGE_PATH = STORAGE_PATH + 'categories/'

PRODUCTS_STORAGE_PATH = STORAGE_PATH + 'products/'


def get_csv_writer(file: TextIOWrapper):
    """Get app's CSV writer with the proper configurations.

    Parameters
    ----------
    file : TextIOWrapper
        File to get the writer with.

    Return
    ------
    _writer : CSV writer.
    """
    return csv.writer(
        file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    )


def get_csv_reader(file: TextIOWrapper):
    """Get app's CSV reader with the proper configurations.

    Parameters
    ----------
    file : TextIOWrapper
        File to get the reader with.

    Return
    ------
    _reader : CSV reader.
    """
    return csv.reader(file, delimiter=',')
