# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from models import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new(wd)
        self.create_contact(wd,
                                Contact(firstname="Vl", lastname="Vakhitov", company="Quality-lab", addreswork="moskov",
                                        mobilenumber="+79143333333",
                                        email="vvakhitov@quality-lab.ru", bday="30",
                                        bmonth="August", byear="1994", address="Irkytsk",
                                        mobilenumber2="+79143679185", notes="test"))
        self.return_home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_new(wd)
        self.create_contact(wd,
                                Contact(firstname="", lastname="", company="", addreswork="",
                                        mobilenumber="",
                                        email="", bday="-",
                                        bmonth="-", byear="", address="",
                                        mobilenumber2="", notes=""))
        self.return_home_page(wd)
        self.logout(wd)


    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_home_page(self, wd):
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd, contact):
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.addreswork)
        wd.find_element_by_name("mobile").send_keys(contact.mobilenumber)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys(contact.address)
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def open_add_new(self, wd):
        # open add new
        wd.find_element_by_link_text("add new").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()

    if __name__ == "__main__":
        unittest.main()
