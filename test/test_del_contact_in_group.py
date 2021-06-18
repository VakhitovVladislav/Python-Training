import random
from model.models import Contact
from model.models import Group


def test_del_contact_in_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vlad", lastname="hater"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = random.choice(old_groups)
    contact = random.choice(db.get_contact_not_in_group())
    if len(db.get_contact_in_group(group.id)) == 0:
        app.contact.add_contact_to_group(contact, group.id)
    old_contact_in_group = db.get_contact_in_group(group.id)
    #assert len(old_contact_in_group) != 0
    app.contact.del_contact_in_group(contact, group.id)
    new_contact_in_group = db.get_contact_in_group(group.id)
    assert len(old_contact_in_group) - 1 == len(new_contact_in_group)