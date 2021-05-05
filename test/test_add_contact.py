# -*- coding: utf-8 -*-
from model.models import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(
                            Contact(firstname="Vl", lastname="Vakhitov", company="Quality-lab", addreswork="moskov",
                                        mobilenumber="+79143333333",
                                        email="vvakhitov@quality-lab.ru", bday="30",
                                        bmonth="August", byear="1994", address="Irkytsk",
                                        mobilenumber2="+79143679185", notes="test"))
    app.session.logout1()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(
                            Contact(firstname="", lastname="", company="", addreswork="",
                                        mobilenumber="",
                                        email="", bday="-",
                                        bmonth="-", byear="", address="",
                                        mobilenumber2="", notes=""))
    app.session.logout1()
