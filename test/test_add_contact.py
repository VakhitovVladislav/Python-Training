# -*- coding: utf-8 -*-
from model.models import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Vl", lastname="Vakhitov", company="Quality-lab", addreswork="Moskow",
                               mobilenumber="+79143333333",
                               email="vvakhitov@quality-lab.ru", bday="30",
                               bmonth="August", byear="1994", address="Irkytsk",
                               notes="test"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", company="", addreswork="",
                               mobilenumber="",
                               email="", bday="-",
                               bmonth="-", byear="", address="",
                               notes=""))
