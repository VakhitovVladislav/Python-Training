from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, middlename=None,  company=None, addreswork=None, all_phones_from_home_page=None,
                 homephone=None,
                 mobilephone=None, workphone=None,
                 email=None, email2=None, email3=None, homepage=None, bday=None,
                 bmonth=None, byear=None, address=None, address2=None, all_emails_from_home_page=None, secondaryphone = None, notes=None, id=None):
        self.firtstname = firstname
        self.middlename = middlename
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.addreswork = addreswork
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address = address
        self.address2 = address2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)



    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) or (self.firstname == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
