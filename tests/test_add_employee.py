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
    page.wait_for_url('https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee')  # Precondition 2
    page.get_by_placeholder('First Name').click()
    page.get_by_placeholder('First Name').clear()
    page.get_by_placeholder('First Name').fill('Jan')  # Step 1
    page.get_by_placeholder('Middle Name').click()
    page.get_by_placeholder('Middle Name').clear()
    page.get_by_placeholder('Middle Name').fill('Piotr')  # Step 2
    page.get_by_placeholder('Last Name').click()
    page.get_by_placeholder('Last Name').clear()
    page.get_by_placeholder('Last Name').fill('Nowak')  # Step 3
    page.locator('form').get_by_role('textbox').nth(4).dblclick()
    page.locator('form').get_by_role('textbox').nth(4).fill('861105')  # Step 4
    page.get_by_role('button', name='Save').click()  # Step 5
    expect(page.get_by_placeholder('First Name')).to_be_visible()
    expect(page.get_by_placeholder('First Name')).to_have_value('Jan')  # Assertion 1
    expect(page.get_by_placeholder('Middle Name')).to_be_visible()
    expect(page.get_by_placeholder('Middle Name')).to_have_value('Piotr')  # Assertion 2
    expect(page.get_by_placeholder('Last Name')).to_be_visible()
    expect(page.get_by_placeholder('Last Name')).to_have_value('Nowak')  # Assertion 3
    expect(page.locator('div').filter(has_text=re.compile(r'^Employee IdOther Id$')).get_by_role(
        'textbox').first).to_be_visible()
    expect(page.locator('div').filter(has_text=re.compile(r'^Employee IdOther Id$')).get_by_role(
        'textbox').first).to_have_value('861105')  # Assertion 4
    expect(page.locator('#app')).to_contain_text('Jan Nowak')  # Assertion 5
