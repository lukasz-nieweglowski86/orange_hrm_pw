class LoginPage:
    login_page_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    index_page_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

    def __init__(self, page):
        self.page = page
        self.username_input_locator = page.get_by_role('textbox', name='username')
        self.password_input_locator = page.get_by_role('textbox', name='password')
        self.login_button_locator = page.get_by_role('button', name='Login')

    def navigate_to_login_page(self):
        self.page.goto(self.login_page_url)
        self.page.wait_for_url(self.login_page_url)

    def enter_username(self, username_value):
        self.username_input_locator.click()
        self.username_input_locator.clear()
        self.username_input_locator.fill(username_value)

    def enter_password(self, password_value):
        self.password_input_locator.click()
        self.password_input_locator.clear()
        self.password_input_locator.fill(password_value)

    def click_login_button(self):
        self.login_button_locator.click()

    def wait_for_index_page_to_load(self):
        self.page.wait_for_url(self.index_page_url)

    def log_in(self, username_value, password_value):
        self.navigate_to_login_page()
        self.enter_username(username_value)
        self.enter_password(password_value)
        self.click_login_button()
        self.wait_for_index_page_to_load()
