from model.models import Contact
import random


def test_add_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="My firstname"))
    old_groups = app.group.get_group_list()
    group = random.choice(old_groups)
    random_contact = random.choice(db.get_contact_not_in_group(group.id))
    random_contact_id = random_contact[11]
    old_contact_in_group = db.get_contacts_in_group(group.id)
    app.contact.add_contact_to_group(random_contact_id, group.id)
    new_contacts_in_group = db.get_contacts_in_group(group.id)
    assert len(old_contact_in_group) + 1 == len(new_contacts_in_group)
    assert (random_contact_id, group.id) in new_contacts_in_group
