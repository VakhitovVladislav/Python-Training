class Contact:

    def __init__(self, firstname=None, lastname=None, company=None, addreswork=None,
                                mobilenumber=None,
                                email=None, bday=None,
                                bmonth=None, byear=None, address=None,
                                mobilenumber2=None, notes=None):
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
        self.mobilenumber2 = mobilenumber2
        self.notes = notes

class Group:

    def __init__(self, name=None, header=None, footer=None):
        self.name = name
        self.header = header
        self.footer = footer