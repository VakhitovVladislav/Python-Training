# -*- coding: utf-8 -*-
from model.models import Contact
from time import sleep


def test_add_contact(app, db, json_contacts, check_ui):
      contact = json_contacts
      old_contacts = db.get_contact_list()
      app.contact.create(contact)
      sleep(10)
      new_contacts = db.get_contact_list()
      old_contacts.append(contact)
      assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
      if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)

