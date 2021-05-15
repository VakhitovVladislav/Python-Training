from model.models import Contact

def test_modify_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New firstname"))

def test_modify_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="New lastname"))

