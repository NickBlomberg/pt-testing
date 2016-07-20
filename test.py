import unittest
from selenium import webdriver
from base import BaseTestCase
import page
from PageObjects import ProjectForm, TaskForm
from data import Data


class LoginTestCase(BaseTestCase):
    """Test cases for the login page"""

    def test_successful_login(self):
        """Test using the correct login credentials"""
        login_page = page.LoginPage(self.driver)
        login_page.check_page_title("Log In")
        login_page.set_email(Data.config["login1"]["user"])
        login_page.set_password(Data.config["login1"]["pass"])
        login_page.click_login_button()

    def test_incorrect_password_login(self):
        """Test using incorrect login credentials will result in an error"""
        login_page = page.LoginPage(self.driver)
        login_page.set_email(Data.config["login2"]["user"])
        login_page.set_password(Data.config["login2"]["pass"])
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
        self.driver.get(Data.config["url"]["project_form"])
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
        self.driver.get(Data.config["url"]["project_form"])

        form = ProjectForm.ProjectForm(self.driver)
        form.set_region(Data.config["project1"]["region"])
        form.set_country(Data.config["project1"]["country"])
        form.set_project_name(Data.config["project1"]["name"])
        form.set_pt_status(Data.config["project1"]["pt_status"])
        form.set_salesperson(Data.config["project1"]["salesperson"])
        form.set_rsm(Data.config["project1"]["rsm"])
        form.set_solution_architect(Data.config["project1"]["solution_architect"])
        form.set_contract_closure(Data.config["project1"]["contract_closure"])
        form.set_contract_currency(Data.config["project1"]["contract_currency"])

        form.click_save_button()
        form.is_creation_successful()
        form.check_user_message('The project has been created.')

    def test_createing_complete_project(self):
        """Create a project with all fields completed"""
        page.LoginPage(self.driver).default_login()
        self.driver.get(Data.config["url"]["project_form"])

        form = ProjectForm.ProjectForm(self.driver)

        # General section
        form.set_salesforce_number(Data.config["project1"]["salesforce"])
        form.set_region(Data.config["project1"]["region"])
        form.set_country(Data.config["project1"]["country"])
        form.set_delivery_customer(Data.config["project1"]["delivery_customer"])
        form.set_channel_partner(Data.config["project1"]["channel_partner"])
        form.set_pa_number(Data.config["project1"]["pa_number"])
        form.set_indirect_salesforce_number(Data.config["project1"]["indirect_salesforce"])
        form.set_project_name(Data.config["project1"]["name"])
        form.set_project_description(Data.config["project1"]["description"])
        form.set_project_description(Data.config["project1"]["no_third_party"])
        form.set_no_third_party()
        form.set_stage(Data.config["project1"]["stage"])
        form.set_pt_status(Data.config["project1"]["pt_status"])
        form.set_status_comment(Data.config["project1"]["status_comment"])
        form.set_main_product(Data.config["project1"]["main_product"])
        form.set_scope(Data.config["project1"]["scope"])
        form.set_revenue_recognition(Data.config["project1"]["revenue_recognition"])

        # Assignments section
        form.set_salesperson(Data.config["project1"]["salesperson"])
        form.set_rsm(Data.config["project1"]["rsm"])
        form.set_sdm(Data.config["project1"]["sdm"])
        form.set_pm(Data.config["project1"]["pm"])
        form.set_solution_architect(Data.config["project1"]["solution_architect"])

        # Contract section
        form.set_contract_type(Data.config["project1"]["contract_type"])
        form.set_contract_closure(Data.config["project1"]["contract_closure"])
        form.set_start_date(Data.config["project1"]["start_date"])
        form.set_end_date(Data.config["project1"]["end_date"])

        # Payment section
        form.set_contract_currency(Data.config["project1"]["contract_currency"])
        form.set_billable_unit(Data.config["project1"]["billable_unit"])
        form.set_contract_amount(Data.config["project1"]["contract_amount"])
        form.set_payment_schedule(Data.config["project1"]["payment_schedule"])
        form.set_payment_comment(Data.config["project1"]["payment_comment"])

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

    def test_creating_full_task(self):
        """Test filling all fields in the task form"""
        page.LoginPage(self.driver).default_login()

        self.driver.get('http://localhost:9000/projects-emea/task-edit?project_id=7290473')
        form = TaskForm.TaskForm(self.driver)

        form.set_task_number(Data.config["task1"]["number"])
        form.set_task_name(Data.config["task1"]["name"])
        form.set_important_information(Data.config["task1"]["important_information"])
        form.set_delivery_address(Data.config["task1"]["delivery_address"])
        form.set_business_unit(Data.config["task1"]["business_unit"])
        form.set_add_solutions(Data.config["task1"]["solutions"])
        form.set_timesheets_required(Data.config["task1"]["timesheets_required"])
        form.set_customer_contact(Data.config["task1"]["customer_contact"])
        form.set_project_manager(Data.config["task1"]["pm"])
        form.set_solution_architect(Data.config["task1"]["solution_architect"])
        form.set_num_units(Data.config["task1"]["units"])
        form.set_labour_rate(Data.config["task1"]["labour_rate"])
        form.set_expense_rate(Data.config["task1"]["expense_rate"])
        form.set_expenses(Data.config["task1"]["expenses"])
        form.set_expense_conditions(Data.config["task1"]["expense_conditions"])
        form.set_autosync_deliveries(Data.config["task1"]["autosync_deliveries"])

        form.click_ok_button()
        form.check_user_message('The project task has been created.')
