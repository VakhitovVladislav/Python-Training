import random
from model.models import Contact


def test_del_contact_in_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vlad", lastname="hater"))
    old_groups = app.group.get_group_list()
    group = random.choice(old_groups)
    random_contact = random.choice(db.get_contact_not_in_group(group))
    random_contact_id = random_contact[0]
    if len(db.get_contact_in_group(group.id)) == 0:
        app.contact.add_contact_to_group(random_contact_id, group.id)
    old_contact_in_group = db.get_contact_in_group(group.id)
    assert len(old_contact_in_group) != 0
    app.contact.del_contact_in_group(random_contact_id, group.id)
    new_contact_in_group = db.get_contact_in_group(group.id)
    assert len(old_contact_in_group) - 1 == len(new_contact_in_group)