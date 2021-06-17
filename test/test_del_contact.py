import random
from model.models import Contact


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vlad", lastname="hater"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(),
                                                                     key=Contact.id_or_max)
