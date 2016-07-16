from page import BasePage
from locators import TaskFormLoc


class TaskForm(BasePage):
    """Provides functions for interaction with a task form"""

    def click_ok_button(self):
        """Click the ok button to save the form"""
        self.driver.find_element(*TaskFormLoc.BUTTON_OK).click()

    def is_task_number_flagged(self):
        """Check task number field for an error"""
        element = self.driver.find_element(*TaskFormLoc.ERROR_TASK_NUMBER)
        assert('Task Number is required' in element.text), \
            'Task number error missing'

    def is_task_name_flagged(self):
        """Check task name field for an error"""
        element = self.driver.find_element(*TaskFormLoc.ERROR_TASK_NAME)
        assert('Task Name is required' in element.text), \
            'Task name error missing'

    def is_busines_unit_flagged(self):
        """Check business unit field for an error"""
        element = self.driver.find_element(*TaskFormLoc.ERROR_BUSINESS_UNIT)
        assert('Business Unit is required' in element.text), \
            'Business unit error missing'
