import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    """Simple base class to provide consitent test case behaviour"""

    def setUp(self):
        """Setup a firefox driver and navigate to index page"""
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:9000/')

    def tearDown(self):
        """Close the browser after running a test by default"""
        self.driver.close()
