from playwright.sync_api import Page


def test_log_in(page: Page) -> None:
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')  # Step 1
    page.get_by_role('textbox', name='username').click()
    page.get_by_role('textbox', name='username').clear()
    page.get_by_role('textbox', name='username').fill('Admin')  # Step 2
    page.get_by_role('textbox', name='password').click()
    page.get_by_role('textbox', name='password').clear()
    page.get_by_role('textbox', name='password').fill('admin123')  # Step 3
    page.get_by_role('button', name='Login').click()  # Step 4
    page.wait_for_url('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
    assert page.url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'  # Assertion 1
