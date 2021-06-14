import pymysql.cursors
from model.models import Group
from model.models import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list



    def destroy(self):
        self.connection.close()


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_in_group(self, group_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, group_id from address_in_groups where group_id=%s",
                (int(group_id),))
            return cursor.fetchall()
        finally:
            cursor.close()

    def get_contact_not_in_group(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select ab.id from addressbook ab "
                "LEFT JOIN address_in_groups ag on ab.id = ag.id where ag.group_id is NULL"
            )
            return cursor.fetchall()
        finally:
            cursor.close()