import selenium.webdriver.support.ui as ui

from base import BasePage
from locators import LoginPageLoc


class LoginPage(BasePage):
    """Define interactions with the login page"""

    def is_title_correct(self):
        """Check if the page title matches expected value"""
        assert 'Log In' in self.driver.title

    def is_login_wrong(self):
        """Check if the login attempt has failed with an error message"""
        assert 'Invalid username or password' in self.driver.page_source

    def set_email(self, email):
        """Set email field"""
        ui.WebDriverWait(self.driver, 5).until(
            lambda driver: self.driver.find_element(*LoginPageLoc.EMAIL)
        )

        self.driver.find_element(*LoginPageLoc.EMAIL).send_keys(email)

    def set_password(self, password):
        """Set password field"""
        ui.WebDriverWait(self.driver, 5).until(
            lambda driver: self.driver.find_element(*LoginPageLoc.PASSWORD)
        )

        self.driver.find_element(*LoginPageLoc.PASSWORD).send_keys(password)

    def click_login_button(self):
        """Click login button"""
        self.driver.find_element(*LoginPageLoc.BUTTON_LOGIN).click()

    def default_login(self):
        """Use login form with default admin account credentials"""
        self.set_email('sharenet.admin@redhat.com')
        self.set_password('redhat')
        self.click_login_button()


class DashboardPage(BasePage):
    """Define interactions with the dashboard page"""
