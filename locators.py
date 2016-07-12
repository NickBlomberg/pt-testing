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
    FIELD_DELIVERY_CUSTOMER = (By.ID, 'customer')
    FIELD_CHANNEL_PARTNER = (By.NAME, 'commercial_customer')
    FIELD_PA_NUMBER = (By.NAME, 'pa_number')
    FIELD_INDIRECT_SALESFORCE_NUMBER = (By.NAME, 'indirect_sf_number')
    FIELD_PROJECT_NAME = (By.ID, 'project_name')
    FIELD_PROJECT_DESCRIPTION = (By.NAME, 'comment')
    FIELD_NO_THIRD_PARTY = (By.NAME, 'no_third_party')
    FIELD_STAGE = (By.NAME, 'stage')
    FIELD_PT_STATUS = (By.ID, 'pt_status')
    FIELD_STATUS_COMMENT = (By.NAME, 'status_comment')
    FIELD_MAIN_PRODUCT = (By.ID, 'main_product_id')
    FIELD_SCOPE = (By.ID, 'scope')
    FIELD_REVENUE_RECOGNITION = (By.NAME, 'revenue_recognition')
    FIELD_SALESPERSON = (By.ID, 'sellers')
    FIELD_RSM = (By.ID, 'engagement_mgr')
    FIELD_SDM = (By.ID, 'program_mgr')
    FIELD_PROJECT_MANAGER = (By.ID, 'project_coordinator')
    FIELD_SOLUTION_ARCHITECT = (By.ID, 'solution_architect')
    FIELD_CONTRACT_TYPE = (By.NAME, 'contract_type')
    FIELD_CONTRACT_CLOSURE = (By.ID, 'f_contract_close')
    FIELD_START_DATE = (By.NAME, 'start_date')
    FIELD_END_DATE = (By.NAME, 'end_date')
    FIELD_CONTRACT_CURRENCY = (By.NAME, 'contract_currency_id')
    FIELD_BILLABLE_UNIT = (By.NAME, 'time_unit')
    FIELD_CONTRACT_AMOUNT = (By.NAME, 'contract_amount')
    FIELD_ACCOUNTING_AMOUNT = (By.NAME, 'acc_contract_amount')
    FIELD_PAYMENT_SCHEDULE = (By.NAME, 'payment')
    FIELD_PAYMENT_COMMENT = (By.NAME, 'payment_comment')

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
