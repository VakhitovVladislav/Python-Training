# -*- coding: utf-8 -*-
from model.models import Group


def test_add_group(app):
    app.group.create(Group(name="zzc", header="zxc", footer="zxc"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
