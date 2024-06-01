class AddEmployeePage:
    add_employee_page_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee'

    def __init__(self, page):
        self.page = page
        self.firstname_input_locator = page.get_by_placeholder('First Name')
        self.middlename_input_locator = page.get_by_placeholder('Middle Name')
        self.lastname_input_locator = page.get_by_placeholder('Last Name')
        self.id_input_locator = page.locator('form').get_by_role('textbox').nth(4)
        self.save_button_locator = page.get_by_role('button', name='Save')

    def navigate_to_add_employee_page(self):
        self.page.goto(self.add_employee_page_url)
        self.page.wait_for_url(self.add_employee_page_url)

    def enter_firstname(self, firstname_value):
        self.firstname_input_locator.click()
        self.firstname_input_locator.clear()
        self.firstname_input_locator.fill(firstname_value)

    def enter_middlename(self, middlename_value):
        self.middlename_input_locator.click()
        self.middlename_input_locator.clear()
        self.middlename_input_locator.fill(middlename_value)

    def enter_lastname(self, lastname_value):
        self.lastname_input_locator.click()
        self.lastname_input_locator.clear()
        self.lastname_input_locator.fill(lastname_value)

    def enter_id(self, id_value):
        self.id_input_locator.click()
        self.id_input_locator.clear()
        self.id_input_locator.fill(id_value)

    def click_save_button(self):
        self.save_button_locator.click()

    def add_employee(self, firstname_value, middlename_value, lastname_value, id_value):
        self.navigate_to_add_employee_page()
        self.enter_firstname(firstname_value)
        self.enter_middlename(middlename_value)
        self.enter_lastname(lastname_value)
        self.enter_id(id_value)
        self.click_save_button()
