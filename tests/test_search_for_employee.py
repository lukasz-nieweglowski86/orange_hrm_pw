from playwright.sync_api import Page, expect
from repo.orange_hrm_pw.pages.login_page import LoginPage
from repo.orange_hrm_pw.data.login_page import LoginPageData
from repo.orange_hrm_pw.pages.add_employee_page import AddEmployeePage
from repo.orange_hrm_pw.data.add_employee_page import AddEmployeePageData
from repo.orange_hrm_pw.pages.employee_list_page import EmployeeListPage


def test_search_for_employee(page: Page) -> None:
    # Preconditions
    LoginPage(page).log_in(LoginPageData.username_value, LoginPageData.password_value)  # Precondition 1
    AddEmployeePage(page).add_employee(AddEmployeePageData.firstname_value,
                                       AddEmployeePageData.middlename_value,
                                       AddEmployeePageData.lastname_value,
                                       AddEmployeePageData.id_value)  # Precondition 2
    EmployeeListPage(page).navigate_to_employee_list_page()  # Precondition 3
    # Steps
    EmployeeListPage(page).enter_employee_id(AddEmployeePageData.id_value)  # Step 1
    EmployeeListPage(page).click_search_button()  # Step 2
    # Assertions
    expect(EmployeeListPage(page).amount_of_results_counter)  # Assertion 1
