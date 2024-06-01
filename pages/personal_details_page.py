import re


class PersonalDetailsPage:

    def __init__(self, page):
        self.page = page
        self.firstname_value_locator = page.get_by_placeholder('First Name')
        self.middlename_value_locator = page.get_by_placeholder('Middle Name')
        self.lastname_value_locator = page.get_by_placeholder('Last Name')
        self.id_value_locator = page.locator('div').filter(has_text=re.compile(r'^Employee IdOther Id$')).get_by_role(
            'textbox').first
        self.first_and_lastname_value_locator = page.locator('#app')
