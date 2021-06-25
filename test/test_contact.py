import re
from model.models import Contact


def test_contacts_info_on_home_page_vs_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vlad", lastname="hater"))
    contact_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for index in range(len(db.get_contact_list())):
        assert contact_from_homepage[index].firstname == contact_from_db[index].firstname
        assert contact_from_homepage[index].lastname == contact_from_db[index].lastname
        assert contact_from_homepage[index].address == contact_from_db[index].address
        assert contact_from_homepage[index].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db[index])
        assert contact_from_homepage[index].all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db[index])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone,  contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


