from model.models import Contact


def test_modify_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Vlad"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New firstname")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Vlad"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(lastname="New lastname"))
#    new_contacts = app.contact.get_contact_list()
#   assert len(old_contacts) == len(new_contacts)

