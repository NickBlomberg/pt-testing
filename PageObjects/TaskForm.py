from selenium.webdriver.support.ui import Select
from base import BasePage
from locators import TaskFormLoc


class TaskForm(BasePage):
    """Provides functions for interaction with a task form"""

    def set_task_number(self, value):
        """Set task number field"""
        self.driver.find_element(*TaskFormLoc.FIELD_TASK_NUMBER).send_keys(value)

    def set_task_name(self, value):
        """Set task name field"""
        self.driver.find_element(*TaskFormLoc.FIELD_TASK_NAME).send_keys(value)

    def set_important_information(self, value):
        """Set important information field"""
        (self.driver.find_element(*TaskFormLoc.FIELD_IMPORTANT_INFORMATION).
            send_keys(value))

    def set_delivery_address(self, value):
        """Set delivery address field"""
        (self.driver.find_element(*TaskFormLoc.FIELD_DELIVERY_ADDRESS).
            send_keys(value))

    def set_business_unit(self, option):
        """Set business unit dropdown"""
        (Select(self.driver.find_element(*TaskFormLoc.FIELD_BUSINESS_UNITS)).
            select_by_visible_text(option))

    def set_add_solutions(self, option):
        """Set add solutions dropdown"""
        (Select(self.driver.find_element(*TaskFormLoc.FIELD_ADD_SOLUTIONS)).
            select_by_visible_text(option))

    def set_timesheets_required(self, check=True):
        """Set timesheets required checkbox"""
        field = self.driver.find_element(*TaskFormLoc.FIELD_TIMESHEETS_REQUIRED)

        if field.is_selected() and not check:
            field.click()

        elif not field.is_selected() and check:
            field.click()

    def set_customer_contact(self, value):
        """Set customer contact field"""
        (self.driver.find_element(*TaskFormLoc.FIELD_CUSTOMER_CONTACT).
            send_keys(value))

    def set_project_manager(self, value):
        """Set project manager field"""
        (self.driver.find_element(*TaskFormLoc.FIELD_PROJECT_MANAGER).
            send_keys(value))

    def set_solution_architect(self, option):
        """Set solution architect dropdown"""
        (Select(self.driver.find_element(*TaskFormLoc.FIELD_SOLUTION_ARCHITECT)).
            select_by_visible_text(option))

    def set_num_units(self, value):
        """Set number of units field"""
        self.driver.find_element(*TaskFormLoc.FIELD_NUM_UNITS).send_keys(value)

    def set_labour_rate(self, value):
        """Set labour rate field"""
        self.driver.find_element(*TaskFormLoc.FIELD_LABOUR_RATE).send_keys(value)

    def set_expense_rate(self, value):
        """Set expense rate field"""
        self.driver.find_element(*TaskFormLoc.FIELD_EXPENSE_RATE).send_keys(value)

    def set_contract_rate_per_unit(self, value):
        """Set contract rate per unit field"""
        field = self.driver.find_element(*TaskFormLoc.FIELD_CONTRACT_RATE)
        field.clear()
        field.send_keys(value)

    def set_accounting_rate_per_unit(self, value):
        """Set accounting rate per unit field"""
        field = self.driver.find_element(*TaskFormLoc.FIELD_ACCOUNTING_RATE)
        field.clear()
        field.send_keys(value)

    def set_expenses(self, option):
        """Set expenses dropdown"""
        (Select(self.driver.find_element(*TaskFormLoc.FIELD_EXPENSES)).
            select_by_visible_text(option))

    def set_expense_conditions(self, value):
        """Set expense conditions field"""
        (self.driver.find_element(*TaskFormLoc.FIELD_EXPENSE_CONDITIONS).
            send_keys(value))

    def set_autosync_deliveries(self, check=True):
        """Set autosync deliveries checkbox"""
        field = self.driver.find_element(*TaskFormLoc.FIELD_AUTOSYNC_DELIVERIES)

        if field.is_selected() and not check:
            field.click()

        elif not field.is_selected() and check:
            field.click()

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
