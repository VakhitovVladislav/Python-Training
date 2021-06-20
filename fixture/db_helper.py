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
            cursor.execute("select id, firstname, lastname, home, mobile, work, "
                           "phone2, address, email, email2,email3 "
                           "from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, home, mobile, work, phone2, address, email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, homephone=home, mobilephone=mobile,
                                                  workphone=work, secondaryphone=phone2, address=address, email=email,
                                                     email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def get_contacts_in_group(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id from address_in_groups")
            return cursor.fetchall()
        finally:
            cursor.close()

    def get_contacts_not_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3, "
                           "phone2 from addressbook where deprecated = '0000-00-00 00:00:00'"
                           "and id not in (select id from address_in_groups)")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=home,
                                    mobilephone=mobile, workphone=work, email=email, email2=email2, email3=email3,
                                    secondaryphone=phone2))
        finally:
            cursor.close()
        return list

    def get_groups_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list "
                           "where group_id in (select group_id from address_in_groups)")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_in_group_by_group_id(self, group_id):
        list = []
        cursor = self.connection.cursor()
        sql = """select id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2 
                 from addressbook where deprecated = '0000-00-00 00:00:00' 
                 and id in (select id from address_in_groups where group_id=%s)"""
        try:
            cursor.execute(sql, (int(group_id),))
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=home,
                                    mobilephone=mobile, workphone=work, email=email, email2=email2, email3=email3,
                                    secondaryphone=phone2))
        finally:
            cursor.close()
        return list

