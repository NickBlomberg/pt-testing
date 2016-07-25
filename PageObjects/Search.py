from selenium.webdriver.common.by import By
from base import BasePage


class Search(BasePage):
    """Provides interaction with the search results page"""

    def click_result(self, n=1):
        """Click the nth result in the list"""

        xpath = "//div[@class='result'][{0}]/div[@class='title']/a".format(n)
        self.driver.find_element(By.XPATH, xpath).click()

    def navigate_to_project(self, pa_number=None, sf_number=None):
        """Navigate to the events page of a project"""

        if pa_number:
            search = 'pa{0}'.format(pa_number)

        elif sf_number:
            search = 'sf {0}'.format(sf_number)

        else:
            raise ValueError("No PA number or Salesforce number provided for navigation")

        self.set_search(search)
        self.click_search_button()
        self.click_result()
