import unittest
from selenium import webdriver
from base import BaseTestCase
import page
from PageObjects import ProjectForm, TaskForm


class LoginTestCase(BaseTestCase):
    """Test cases for the login page"""

    def test_successful_login(self):
        """Test using the correct login credentials"""
        login_page = page.LoginPage(self.driver)
        login_page.check_page_title("Log In")
        login_page.set_email('sharenet.admin@redhat.com')
        login_page.set_password('redhat')
        login_page.click_login_button()

    def test_incorrect_password_login(self):
        """Test using incorrect login credentials will result in an error"""
        login_page = page.LoginPage(self.driver)
        login_page.set_email('sharenet.admin@redhat.com')
        login_page.set_password('wrong')
        login_page.click_login_button()
        login_page.is_login_wrong()


class DashboardTestCase(BaseTestCase):
    """Test cases for the dashboard page"""

    def test_dashboard_title(self):
        """Check the dashboard page title meets expected value"""
        page.LoginPage(self.driver).default_login()

        dashboard_page = page.DashboardPage(self.driver)
        dashboard_page.check_page_title("Project Tracker")


class ProjectFormTestCase(BaseTestCase):
    """Test cases for the project form"""

    def test_blank_form_submit(self):
        """Test submitting blank form results in flagged mandatory fields"""
        page.LoginPage(self.driver).default_login()
        self.driver.get('http://localhost:9000/projects-emea/project-edit')
        self.driver.implicitly_wait(5)

        form = ProjectForm.ProjectForm(self.driver)
        form.click_save_button()

        # form.is_region_flagged() TODO find out why region is being preset
        form.is_country_flagged()
        form.is_project_name_flagged()
        form.is_pt_status_flagged()
        form.is_salesperson_flagged()
        # form.is_rsm_flagged() TODO find out why RSM is being preset
        form.is_solution_architect_flagged()
        form.is_contract_close_flagged()
        form.is_contract_currency_flagged()

    def test_creating_simple_project(self):
        """Test creating a project with minimum fields completed"""
        page.LoginPage(self.driver).default_login()
        self.driver.get('http://localhost:9000/projects-emea/project-edit')

        form = ProjectForm.ProjectForm(self.driver)
        form.set_region('DA')
        form.set_country('Germany')
        form.set_project_name('Selenium Test Project')
        form.set_pt_status('Active')
        form.set_salesperson('Alexander Picker (DA, Munich)')
        form.set_rsm('Mark Schulze')
        form.set_solution_architect('Rhys Oxenham (UKIE, Farnborough) [530308]')
        form.set_contract_closure('10 Jul 2016')
        form.set_contract_currency('EUR')

        form.click_save_button()
        form.is_creation_successful()
        form.check_user_message('The project has been created.')

    def test_createing_complete_project(self):
        """Create a project with all fields completed"""
        page.LoginPage(self.driver).default_login()
        self.driver.get('http://localhost:9000/projects-emea/project-edit')

        form = ProjectForm.ProjectForm(self.driver)
        form.set_salesforce_number('393939')
        form.set_region('UKIE')
        form.set_country('United Kingdom')
        form.set_delivery_customer('QA-TESCO, United Kingdom [5665828]')
        form.set_channel_partner('Amadeus, Germany [7276922]')
        form.set_pa_number('939393')
        form.set_indirect_salesforce_number('339339')
        form.set_project_name('Test: complete project')
        form.set_project_description('Test: project description')
        form.set_no_third_party()
        form.set_stage('Current')
        form.set_pt_status('Active')
        form.set_status_comment('Test: status comment')
        form.set_main_product('RHEL')
        form.set_scope('GPS')
        form.set_revenue_recognition('Consulting Units')
        form.set_salesperson('Alexander Picker (DA, Munich)')
        form.set_rsm('Mark Schulze')
        form.set_sdm('Eric Lavarde (DA, Stuttgart) [1835157]')
        form.set_pm('Irena Pribova (Nordics, Stockholm) [2144168]')
        form.set_solution_architect('Rhys Oxenham (UKIE, Farnborough) [530308]')
        form.set_contract_type('T&M Hourly')
        form.set_contract_closure('12 Jul 2016')
        form.set_start_date('12 Jul 2016')
        form.set_end_date('11 Jul 2017')
        form.set_contract_currency('EUR')
        form.set_billable_unit('Hour')
        form.set_contract_amount('100')
        form.set_payment_schedule('monthly')
        form.set_payment_comment('Test: payment comment')

        form.click_save_button()
        form.is_creation_successful()
        form.check_user_message('The project has been created.')


class TaskFormTestCase(BaseTestCase):
    """Test functionality related to the task form"""
    def test_blank_form_submit(self):
        page.LoginPage(self.driver).default_login()

        self.driver.get('http://localhost:9000/projects-emea/task-edit?project_id=7290473')
        form = TaskForm.TaskForm(self.driver)
        form.click_ok_button()

        form.is_task_number_flagged()
        form.is_task_name_flagged()
        form.is_busines_unit_flagged()
