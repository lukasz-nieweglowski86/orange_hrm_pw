from playwright.sync_api import Page, expect
from repo.orange_hrm_pw.pages.login_page import LoginPage
from repo.orange_hrm_pw.data.login_page import LoginPageData
from repo.orange_hrm_pw.pages.add_employee_page import AddEmployeePage
from repo.orange_hrm_pw.data.add_employee_page import AddEmployeePageData
from repo.orange_hrm_pw.pages.personal_details_page import PersonalDetailsPage


def test_add_employee(page: Page) -> None:
    # Preconditions
    LoginPage(page).log_in(LoginPageData.username_value, LoginPageData.password_value)  # Precondition 1
    AddEmployeePage(page).navigate_to_add_employee_page()  # Precondition 2
    # Steps
    AddEmployeePage(page).enter_firstname(AddEmployeePageData.firstname_value)  # Step 1
    AddEmployeePage(page).enter_middlename(AddEmployeePageData.middlename_value)  # Step 2
    AddEmployeePage(page).enter_lastname(AddEmployeePageData.lastname_value)  # Step 3
    AddEmployeePage(page).enter_id(AddEmployeePageData.id_value)  # Step 4
    AddEmployeePage(page).click_save_button()  # Step 5
    # Assertions
    expect(PersonalDetailsPage(page).firstname_value_locator).to_be_visible()
    expect(PersonalDetailsPage(page).firstname_value_locator).to_have_value(
        AddEmployeePageData.firstname_value)  # Assertion 1
    expect(PersonalDetailsPage(page).middlename_value_locator).to_be_visible()
    expect(PersonalDetailsPage(page).middlename_value_locator).to_have_value(
        AddEmployeePageData.middlename_value)  # Assertion 2
    expect(PersonalDetailsPage(page).lastname_value_locator).to_be_visible()
    expect(PersonalDetailsPage(page).lastname_value_locator).to_have_value(
        AddEmployeePageData.lastname_value)  # Assertion 3
    expect(PersonalDetailsPage(page).id_value_locator).to_be_visible()
    expect(PersonalDetailsPage(page).id_value_locator).to_have_value(
        AddEmployeePageData.id_value)  # Assertion 4
    expect(PersonalDetailsPage(page).first_and_lastname_value_locator).to_contain_text(
        AddEmployeePageData.firstname_value + ' ' + AddEmployeePageData.lastname_value)  # Assertion 5
