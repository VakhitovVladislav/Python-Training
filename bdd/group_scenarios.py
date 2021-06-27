

from pytest_bdd import scenario
from .group_steps_py import *

@scenario('group.feature', 'Add new group')
def test_add_new_group():
    pass

@scenario('group.feature', 'Delete a group')
def test_delete_group():
    pass