# -*- coding: utf-8 -*-
from model.models import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Vl", lastname="Vakhitov", company="Quality-lab", addreswork="Moskow",
                               mobilenumber="+79143333333",
                               email="vvakhitov@quality-lab.ru", bday="30",
                               bmonth="August", byear="1994", address="Irkytsk",
                               notes="test")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", lastname="", company="", addreswork="",
                               mobilenumber="",
                               email="", bday="-",
                               bmonth="-", byear="", address="",
                               notes="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
