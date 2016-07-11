from selenium.webdriver.common.by import By


class GlobalLoc(object):
    """Provide locators for elements found on every page"""
    USER_MESSAGE = (By.XPATH, '//div[./@id="user-message"]/ul/li')


class LoginPageLoc(object):
    """Provide locators for elements found in the login page"""
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    BUTTON_LOGIN = (By.NAME, 'formbutton:ok')


class ProjectFormLoc(object):
    """Provide locators for elements found in the project form"""
    FIELD_SALESFORCE_NUMBER = (By.ID, 'sf_number')
    FIELD_REGION = (By.ID, 'region_id')
    FIELD_COUNTRY = (By.ID, 'country')
    FIELD_PROJECT_NAME = (By.ID, 'project_name')
    FIELD_PT_STATUS = (By.ID, 'pt_status')
    FIELD_SALESPERSON = (By.ID, 'sellers')
    FIELD_RSM = (By.ID, 'engagement_mgr')
    FIELD_SOLUTION_ARCHITECT = (By.ID, 'solution_architect')
    FIELD_CONTRACT_CLOSURE = (By.ID, 'f_contract_close')
    FIELD_CONTRACT_CURRENCY = (By.NAME, 'contract_currency_id')

    ERROR_REGION = (By.XPATH, '//div[./@id="region_select_div"]'
                    '/following::div[@class="form-error"][1]')

    ERROR_COUNTRY = (By.XPATH, '//select[./@id="country"]'
                     '/following-sibling::div[1]')

    ERROR_PROJECT_NAME = (By.XPATH, '//input[./@id="project_name"]'
                          '/following-sibling::div[1]')

    ERROR_PT_STATUS = (By.XPATH, '//select[./@id="pt_status"]'
                       '/following-sibling::div[1]')

    ERROR_SALESPERSON = (By.XPATH, '//select[./@id="sellers"]'
                         '/following-sibling::div[1]')

    ERROR_RSM = (By.XPATH, '//select[./@id="engagement_mgr"]'
                 '/following-sibling::div[1]')

    ERROR_SA = (By.XPATH, '//input[./@id="solution_architect"]'
                          '/following::div[@class="form-error"][1]')

    ERROR_CONTRACT_CLOSE = (By.XPATH, '//input[./@id="f_contract_close"]'
                            '/following::div[1]')

    ERROR_CONTRACT_CUR = (By.XPATH, '//select[./@name="contract_currency_id"]/'
                          'following-sibling::div[1]')

    BUTTON_SAVE = (By.NAME, 'formbutton:save')
