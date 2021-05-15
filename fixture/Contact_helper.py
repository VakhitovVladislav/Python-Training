from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_value("firstname", contact.firstname)
        self.change_contact_value("lastname", contact.lastname)
        self.change_contact_value("company", contact.company)
        self.change_contact_value("address", contact.addreswork)
        self.change_contact_value("mobile", contact.mobilenumber)
        self.change_contact_value("email", contact.email)
        self.change_born_value("bday", contact.bday)
        self.change_born_value("bmonth", contact.bmonth)
        self.change_contact_value("byear", contact.byear)
        self.change_contact_value("address", contact.address)
        self.change_contact_value("notes", contact.notes)

    def change_born_value(self, field_day, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_day).click()
            Select(wd.find_element_by_name(field_day)).select_by_visible_text(text)

    def change_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_home_page()
        # open_modification_form
        wd.find_element_by_xpath("(//img[@alt='Edit'])[1]").click()
        # fill_contact_form
        self.fill_contact_form(new_contact_data)
        # update_contact
        wd.find_element_by_name("update").click()
        self.return_home_page()

    def open_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
