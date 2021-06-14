from fixture.orm import ORMFixture
from model.models import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    L = db.get_contacts_in_not_group(Group(id="22"))
    for item in L:
        print(item)
    print(len(L))
finally:
    pass #db.destroy()