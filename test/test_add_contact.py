# -*- coding: utf-8 -*-
from model.models import Contact
import pytest
import random
import string


def random_phone_number():
    phone_list = ['914', '983', '902', '999', '950', '924']
    return "+" + random.choice(phone_list) + "".join([random.choice(string.digits) for i in range(7)])


def random_email(maxlen):
    email = string.ascii_letters + " "
    email_list = ["quality-lab.ru", "@google.com", "@yandex.ru", "@rambler.ru", "@mail.ru"]
    return "".join([random.choice(email) for i in range(random.randrange(maxlen))]) + random.choice(email_list)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20),
                    lastname=random_string("lastname", 20), company=random_string("company", 10), addreswork=random_string("addreswork", 20),
                    homephone=random_phone_number(), mobilephone=random_phone_number(),
                    workphone=random_phone_number(), email=random_email(10), email2=random_email(10),
                    email3=random_email(8), bday="30", bmonth="August", byear="1994", address=random_string("address", 10), address2="vampilov",
                    secondaryphone=random_phone_number(), notes=random_string("notes", 50))
            for i in range(2)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
      old_contacts = app.contact.get_contact_list()
      app.contact.create(contact)
      assert len(old_contacts) + 1 == app.contact.count()
      new_contacts = app.contact.get_contact_list()
      old_contacts.append(contact)
      assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

