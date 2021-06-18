from model.models import Contact
from model.models import Group
import random


def test_add_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vlad", lastname="hater"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_not_in_group()) == 0:
        app.contact.create(Contact(firstname="Vlad", lastname="hater"))
    old_groups = app.group.get_group_list()
    random_group = random.choice(old_groups)
    group_db_id = random_group.id
    contacts_not_in_group = db.get_contact_not_in_group()
    random_contact = random.choice(contacts_not_in_group)
    random_contact_id = random_contact[0]
    old_contact_in_group = db.get_contact_in_group(group_db_id)
    app.contact.add_contact_to_group(random_contact_id, group_db_id)
    new_contacts_in_group = db.get_contact_in_group(group_db_id)
    assert len(old_contact_in_group) + 1 == len(new_contacts_in_group)
