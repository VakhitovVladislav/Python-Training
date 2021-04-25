# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_add_new(wd)
        self.create_contact(wd)
        self.return_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_home_page(self, wd):
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd):
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Vl")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Vakhitov")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("Work")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Quality-lab")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("moskow")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("+79143333333")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("+79146666666")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("vvakhitov@quality-lab.ru")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("siemiens11@gmail.com")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("30")
        wd.find_element_by_xpath("//option[@value='30']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("August")
        wd.find_element_by_xpath("//option[@value='August']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1994")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("Irkytsk")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("Vampolova")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("test")
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_add_new(self, wd):
        # open add new
        wd.find_element_by_link_text("add new").click()

    def login(self, wd):
        # login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
