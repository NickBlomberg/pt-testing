import unittest
from selenium import webdriver


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
