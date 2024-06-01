import re


class EmployeeListPage:
    employee_list_page_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'

    def __init__(self, page):
        self.page = page
        self.employee_id_value_locator = page.get_by_role('textbox').nth(2)
        self.search_button_locator = page.get_by_role('button', name='Search')
        self.amount_of_results_counter = page.locator('div').filter(has_text=re.compile(r'^\(1\) Record Found$')).nth(1)

    def navigate_to_employee_list_page(self):
        self.page.goto(self.employee_list_page_url)
        self.page.wait_for_url(self.employee_list_page_url)

    def enter_employee_id(self, employee_id_value):
        self.employee_id_value_locator.click()
        self.employee_id_value_locator.clear()
        self.employee_id_value_locator.fill(employee_id_value)

    def click_search_button(self):
        self.search_button_locator.click()

    def search_for_employee_by_id(self, employee_id_value):
        self.navigate_to_employee_list_page()
        self.enter_employee_id(employee_id_value)
        self.click_search_button()
