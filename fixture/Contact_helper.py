from selenium.webdriver.support.ui import Select
from model.models import Contact
import re
import random

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def return_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(
                wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_contact_value("firstname", contact.firstname)
        self.change_contact_value("middlename", contact.middlename)
        self.change_contact_value("lastname", contact.lastname)
        self.change_contact_value("company", contact.company)
        self.change_contact_value("address", contact.addreswork)
        self.change_contact_value("home", contact.homephone)
        self.change_contact_value("mobile", contact.mobilephone)
        self.change_contact_value("work", contact.workphone)
        self.change_contact_value("email", contact.email)
        self.change_contact_value("email2", contact.email2)
        self.change_contact_value("email3", contact.email3)
        self.change_contact_value("homepage", contact.homepage)
        self.change_born_value("bday", contact.bday)
        self.change_born_value("bmonth", contact.bmonth)
        self.change_contact_value("byear", contact.byear)
        self.change_contact_value("address", contact.address)
        self.change_contact_value("address2", contact.address2)
        self.change_contact_value("phone2", contact.secondaryphone)
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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()



    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_home_page()
        # open_modification_form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill_contact_form
        self.fill_contact_form(new_contact_data)
        # update_contact
        wd.find_element_by_name("update").click()
        self.home_page()
        self.contact_cache = None


    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.return_home_page()
        # open_modification_form
        wd.find_element_by_css_selector(f"a[href='edit.php?id={id}']").click()
        # fill_contact_form
        self.fill_contact_form(new_contact_data)
        # update_contact
        wd.find_element_by_name("update").click()
        self.home_page()
        self.contact_cache = None

    def open_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)




    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_elements_by_xpath("//img[@alt='Edit']")[index].click()


    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                                                  workphone=workphone, secondaryphone=secondaryphone, address=address, email=email,
                                                     email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)",text).group(1)
        mobilephone = re.search("M: (.*)",text).group(1)
        workphone = re.search("W: (.*)",text).group(1)
        secondaryphone = re.search("P: (.*)",text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.return_home_page()
        self.select_contact_by_id(contact_id)
        self.select_group_to_add_by_id(group_id)
        wd.find_element_by_name("add").click()
        self.return_home_page()

    def del_contact_in_group(self, contact_id, group_id):
        wd = self.app.wd
        self.return_home_page()
        self.select_group_to_add_by_id(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()
        self.return_home_page()

    def select_group_to_add_by_id(self, id):
        wd = self.app.wd
        zzz=[]
        wd = self.app.wd
        wd.find_element_by_css_selector("select[name='to_group']").click()
        zzz.append(wd.find_element_by_css_selector("select[name='to_group'] option[value='%s']" % id).click())
        return zzz
