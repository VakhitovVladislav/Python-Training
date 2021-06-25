import random
from model.models import Contact
from model.models import Group


def test_del_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vlad", lastname="hater"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = db.get_groups_with_contacts()
    group = random.choice(groups)
    group_id = group.id
    contacts = db.get_contacts_in_group()
    contact = random.choice(contacts)
    contact_id = contact.id
    if len(db.get_contacts_in_group()) == 0:
        app.contact.add_contact_to_group(contact_id, group_id)
    old_contacts = db.get_contacts_in_group()
    app.contact.del_contact_in_group(contact_id, group_id)
    new_contacts = db.get_contacts_in_group()
    assert len(old_contacts) - 1 == len(new_contacts)

