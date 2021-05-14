from model.models import Contact

def test_modify_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New firstname"))
    app.session.logout()


def test_modify_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="New lastname"))
    app.session.logout()
