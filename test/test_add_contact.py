# -*- coding: utf-8 -*-
from model.models import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Vl", middlename= "VL",  lastname="Vakhitov", company="Quality-lab", addreswork="Moskow",
                                homephone="+7143679185", mobilephone="+7914333333", workphone="+7144444444",
                                email="vvakhitov@quality-lab.ru", email2 = "strr@gmail.com", email3 = "sss@yandex.ru", bday="30",
                               bmonth="August", byear="1994", address="Irkytsk", address2="vampilov", secondaryphone="+7145555555",
                               notes="test")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", lastname="", company="", addreswork="",
#                               mobilenumber="",
#                               email="", bday="-",
#                               bmonth="-", byear="", address="",
#                               notes="")
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
