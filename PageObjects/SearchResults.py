from selenium.webdriver.common.by import By
from page import BasePage


class SearchResults(BasePage):
    """Provides interaction with the search results page"""

    def click_result(self, n=1):
        """Click the nth result in the list"""

        xpath = "//div[@class='result'][{0}]/div[@class='title']/a".format(n)
        self.driver.find_element(By.XPATH, xpath).click()
