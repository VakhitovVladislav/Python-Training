from fixture.orm import ORMFixture
from fixture.db_helper import DbFixture
from model.models import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()
