from playwright.sync_api import Page
from repo.orange_hrm_pw.pages.login_page import LoginPage
from repo.orange_hrm_pw.data.login_page import LoginPageData


def test_log_in(page: Page) -> None:
    # Steps
    LoginPage(page).navigate_to_login_page()  # Step 1
    LoginPage(page).enter_username(LoginPageData.username_value)  # Step 2
    LoginPage(page).enter_password(LoginPageData.password_value)  # Step 3
    LoginPage(page).click_login_button()  # Step 4
    # Assertions
    LoginPage(page).wait_for_index_page_to_load()
    assert page.url == LoginPage.index_page_url  # Assertion 1
