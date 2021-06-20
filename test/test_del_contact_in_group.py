import random
from model.models import Contact
from model.models import Group


def test_del_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vlad", lastname="hater"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contacts_in_group()) ==0:
        app.contact.add_contact_to_group()
    groups = db.get_groups_with_contacts()
    group = random.choice(groups)
    group_id = group.id
    contacts = db.get_contacts_in_group()
    contact = random.choice(contacts)
    contact_id = contact.id
    old_contacts = db.get_contacts_in_group()
    app.contact.del_contact_in_group(contact_id, group_id)
    new_contacts = db.get_contacts_in_group()
    assert len(old_contacts) - 1 == len(new_contacts)















#    groups = db.get_groups_with_contacts()
#    group = random.choice(groups)
#    contacts = db.get_contact_in_group(group.id)
#    contact = random.choice(contacts)
#    app.contact.del_contact_in_group(contact.id, group.id)
#    groups = db.get_groups_with_contacts()
#    group = random.choice(groups)
#    old_contacts = db.get_contacts_in_group()
#    contacts_from_group = db.get_contacts_in_group_by_group_id(group.id)
#    contact = random.choice(contacts_from_group)
#    app.contact.del_contact_from_group(contact.id, group.id)
#    new_contacts = db.get_contacts_in_group()
#    assert len(old_contacts) - 1 == len(new_contacts)
#    if check_ui:
#        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)




#    old_groups = app.group.get_group_list()
#    random_group = random.choice(old_groups)
#    contact = random.choice(db.get_contact_in_group())
#    if len(db.get_contact_in_group(group.id)) == 0:
#        app.contact.del_contact_in_group(contact, group.id)
#    old_contact_in_group = db.get_contact_in_group(group.id)
#    #assert len(old_contact_in_group) != 0
#    app.contact.del_contact_in_group(contact, group.id)
#    new_contact_in_group = db.get_contact_in_group(group.id)
#    assert len(old_contact_in_group) - 1 == len(new_contact_in_group)