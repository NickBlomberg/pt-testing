import unittest
from selenium import webdriver

from locators import GlobalLoc


class BaseTestCase(unittest.TestCase):
    """Simple base class to provide consitent test case behaviour"""

    def __init__(self, *args, **kwargs):
        super(BaseTestCase, self).__init__(*args, **kwargs)
        self.base_url = 'http://localhost:9000'

    def setUp(self):
        """Setup a firefox driver and navigate to index page"""
        self.driver = webdriver.Firefox()
        self.driver.get(self.base_url)

    def tearDown(self):
        """Close the browser after running a test by default"""
        self.driver.close()


class BasePage(object):
    """Defines a simple page base class"""

    def __init__(self, driver):
        self.driver = driver

    def check_user_message(self, expected):
        """Check if the expected user message is displayed"""
        actual = self.driver.find_element(*GlobalLoc.USER_MESSAGE).text
        assert(expected in actual)

    def check_page_title(self, expected):
        """Check that the browser title matches expected value"""
        assert expected == self.driver.title

    def set_search(self, keywords):
        """Set search field"""
        field = self.driver.find_element(*GlobalLoc.FIELD_SEARCH)
        field.clear()
        field.send_keys(keywords)

    def click_search_button(self):
        """Click the search Go button"""
        self.driver.find_element(*GlobalLoc.BUTTON_SEARCH).click()
