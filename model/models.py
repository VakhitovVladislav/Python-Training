from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, company=None, addreswork=None,
                 mobilenumber=None,
                 email=None, bday=None,
                 bmonth=None, byear=None, address=None, notes=None, id=None):
        self.firtstname = firstname
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.addreswork = addreswork
        self.mobilenumber = mobilenumber
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address = address
        self.notes = notes
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
