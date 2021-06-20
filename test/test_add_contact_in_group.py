from model.models import Contact
from model.models import Group
import random


def test_add_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vlad", lastname="hater"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contacts_not_in_group()) == 0:
        app.contact.create(Contact(firstname="Vlad", lastname="hater"))
    group = app.group.get_group_list()
    groups = random.choice(group)
    group_id = groups.id
    contacts = app.contact.get_contact_list()
    contact = random.choice(contacts)
    contact_id = contact.id
    old_contact_in_group = db.get_contacts_in_group()
    app.contact.add_contact_to_group(contact_id, group_id)
    new_contacts_in_group = db.get_contacts_in_group()
    assert len(old_contact_in_group) + 1 == len(new_contacts_in_group)
