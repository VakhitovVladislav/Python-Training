class Contact:

    def __init__(self, firstname, lastname, company, addreswork,
                                mobilenumber,
                                email, bday,
                                bmonth, byear, address,
                                mobilenumber2, notes):
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

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer