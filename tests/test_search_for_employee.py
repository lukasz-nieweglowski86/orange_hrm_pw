import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.get_by_role('textbox', name='username').click()
    page.get_by_role('textbox', name='username').clear()
    page.get_by_role('textbox', name='username').fill('Admin')
    page.get_by_role('textbox', name='password').click()
    page.get_by_role('textbox', name='password').clear()
    page.get_by_role('textbox', name='password').fill('admin123')
    page.get_by_role('button', name='Login').click()
    page.wait_for_url('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
    # adding user
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee')
    page.wait_for_url('https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee')
    page.get_by_placeholder('First Name').click()
    page.get_by_placeholder('First Name').clear()
    page.get_by_placeholder('First Name').fill('Jan')
    page.get_by_placeholder('Middle Name').click()
    page.get_by_placeholder('Middle Name').clear()
    page.get_by_placeholder('Middle Name').fill('Piotr')
    page.get_by_placeholder('Last Name').click()
    page.get_by_placeholder('Last Name').clear()
    page.get_by_placeholder('Last Name').fill('Nowak')
    page.locator('form').get_by_role('textbox').nth(4).dblclick()
    page.locator('form').get_by_role('textbox').nth(4).fill('861105')
    page.get_by_role('button', name='Save').click()
    # searching for user
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList')
    page.wait_for_url('https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList')  # Precondition 1
    page.get_by_role('textbox').nth(2).click()
    page.get_by_role('textbox').nth(2).clear()
    page.get_by_role('textbox').nth(2).fill('861105')  # Step 1
    page.get_by_role('button', name='Search').click()  # Step 2
    expect(page.locator('div').filter(has_text=re.compile(r'^\(1\) Record Found$')).nth(1))  # Assertion 1
