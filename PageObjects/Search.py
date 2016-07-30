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

    def navigate_to_task(self, task_number=None, pa_number=None, sf_number=None):
        """
        Assist with navigation to the tasks section of a project. If no task number is
        provided, direct the browser to the list of tasks. Otherwise, open the
        requested task in the edit form.
        """
        if not isinstance(task_number, (int, long, type(None))):
            raise ValueError("Invalid task number provided for navigation")

        self.navigate_to_project(pa_number, sf_number)

        # Click link to reach the tasks list
        xpath_tasks = "//td[text()='Project Name']/following::td[1]//a[text()='tasks']"
        self.driver.find_element(By.XPATH, xpath_tasks).click()

        if task_number == None:
            return

        # Click edit button for the requested task
        xpath_edit = "//table[./@class='list']//tr/td[contains(text(), '{0} -')]/\
                    preceding::a[text()='edit'][1]".format(task_number)
        self.driver.find_element(By.XPATH, xpath_edit).click()
