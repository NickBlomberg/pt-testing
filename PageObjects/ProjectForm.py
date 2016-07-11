from selenium.webdriver.support.ui import Select
from page import BasePage
from locators import ProjectFormLoc


class ProjectForm(BasePage):
    """Define interaction with the project form"""

    def set_salesforce_number(self, value):
        """Set Salesforce Opportunity # field"""
        (self.driver.find_element(*ProjectFormLoc.FIELD_SALESFORCE_NUMBER).
            send_keys(value))

    def set_region(self, option):
        """Set region dropdown"""
        (Select(self.driver.find_element(*ProjectFormLoc.FIELD_REGION)).
            select_by_visible_text(option))

    def set_country(self, option):
        """Set country dropdown"""
        (Select(self.driver.find_element(*ProjectFormLoc.FIELD_COUNTRY)).
            select_by_visible_text(option))

    def set_project_name(self, value):
        """Set project name field"""
        (self.driver.find_element(*ProjectFormLoc.FIELD_PROJECT_NAME).
            send_keys(value))

    def set_pt_status(self, option):
        """Set pt status dropdown"""
        (Select(self.driver.
                find_element(*ProjectFormLoc.FIELD_PT_STATUS)).
            select_by_visible_text(option))

    def set_salesperson(self, option):
        """Set salesperson dropdown"""
        (Select(self.driver.
                find_element(*ProjectFormLoc.FIELD_SALESPERSON)).
            select_by_visible_text(option))

    def set_rsm(self, value):
        """Set regional services manager field"""
        (self.driver.find_element(*ProjectFormLoc.FIELD_RSM).
            send_keys(value))

    def set_solution_architect(self, value):
        """Set solution architect field"""
        (self.driver.find_element(*ProjectFormLoc.FIELD_SOLUTION_ARCHITECT).
            send_keys(value))

    def set_contract_closure(self, value):
        """Set contract closure date field"""
        (self.driver.find_element(*ProjectFormLoc.FIELD_CONTRACT_CLOSURE).
            send_keys(value))

    def set_contract_currency(self, option):
        """Set contract currency dropdown"""
        (Select(self.driver.
                find_element(*ProjectFormLoc.FIELD_CONTRACT_CURRENCY)).
            select_by_visible_text(option))

    def click_save_button(self):
        """Click form save button"""
        self.driver.find_element(*ProjectFormLoc.BUTTON_SAVE).click()

    def is_region_flagged(self):
        """Check region field for an error"""
        element = self.driver.find_element(*ProjectFormLoc.ERROR_REGION)
        assert('Region is required' in element.text), 'Region error missing'

    def is_country_flagged(self):
        """Check country field for an error"""
        element = self.driver.find_element(*ProjectFormLoc.ERROR_COUNTRY)
        assert('Country is required' in element.text), 'Country error missing'

    def is_project_name_flagged(self):
        """Check project name field for an error"""
        element = self.driver.find_element(*ProjectFormLoc.ERROR_PROJECT_NAME)
        assert('Project Name is required' in element.text), \
            'Project name error missing'

    def is_pt_status_flagged(self):
        """Check pt status field for an error"""
        element = self.driver.find_element(*ProjectFormLoc.ERROR_PT_STATUS)
        assert('PT Status is required' in element.text), \
            'PT status error missing'

    def is_salesperson_flagged(self):
        """Check salesperson field for an error"""
        element = self.driver.find_element(*ProjectFormLoc.ERROR_SALESPERSON)
        assert('If the Scope is not INT, the Sales Person must be specified.'
               in element.text), 'Salesperson error missing'

    def is_rsm_flagged(self):
        """Check regional services manager field for an error"""
        element = self.driver.find_element(*ProjectFormLoc.ERROR_RSM)
        assert('Regional Services Manager is required' in element.text), \
            'RSM error missing'

    def is_solution_architect_flagged(self):
        """Check solution architect field for and error"""
        element = self.driver.find_element(*ProjectFormLoc.ERROR_SA)
        assert('If the Scope is not INT, the '
               'Solution Architect must be specified.'
               in element.text), 'SA error missing'

    def is_contract_close_flagged(self):
        """Check contract close date field for an error"""
        element = self.driver.find_element(*ProjectFormLoc.ERROR_CONTRACT_CLOSE)
        assert('If the Scope is not INT, the Contract '
               'Closure date must be specified.'
               in element.text), 'Contract close error missing'

    def is_contract_currency_flagged(self):
        """Check contract currency field for an error"""
        element = self.driver.find_element(*ProjectFormLoc.ERROR_CONTRACT_CUR)
        assert('If the Scope is not INT, the Contract '
               'Currency must be specified.'
               in element.text), 'Contract currency error missing'

    def is_creation_successful(self):
        """Check if a project has been sucessfully created"""
        assert 'Project Created' in self.driver.title

        assert '<h1 class="page-title">Project Created</h1>' \
            in self.driver.page_source, 'Project Created title missing'

        assert '<h2>Financial Quarters</h2>' \
            in self.driver.page_source, 'Financial Quarters title missing'

        assert '<h2>Tasks</h2>' \
            in self.driver.page_source, 'Tasks title missing'

        assert '<h2>Central Proposal Board Escalation</h2>' \
            in self.driver.page_source, 'CPB title missing'
