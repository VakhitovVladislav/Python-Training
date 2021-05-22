from selenium import webdriver
from fixture.session import SessionHelper
from fixture.Contact_helper import ContactHelper
from fixture.Group_helper import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.wd.quit()
