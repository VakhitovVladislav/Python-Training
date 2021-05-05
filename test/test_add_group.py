# -*- coding: utf-8 -*-
from model.models import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="zzc", header="zxc", footer="zxc"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

