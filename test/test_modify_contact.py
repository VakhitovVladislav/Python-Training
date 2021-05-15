from model.models import Contact

def test_modify_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Vlad"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))

def test_modify_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Vlad"))
    app.contact.modify_first_contact(Contact(lastname="New lastname"))

