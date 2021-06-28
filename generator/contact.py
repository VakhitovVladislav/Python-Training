from model.models import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["Number_of_contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_phone_number():
    phone_list = ['914', '983', '902', '999', '951', '924', '953']
    return "+" + random.choice(phone_list) + "".join([random.choice(string.digits) for i in range(7)])


def random_email(maxlen):
    email = string.ascii_letters + " "
    email_list = ["quality-lab.ru", "@google.com", "@yandex.ru", "@rambler.ru", "@mail.ru"]
    return "".join([random.choice(email) for i in range(random.randrange(maxlen))]) + random.choice(email_list)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20),
                    lastname=random_string("lastname", 20), company=random_string("company", 10), addreswork=random_string("addreswork", 20),
                    homephone=random_phone_number(), mobilephone=random_phone_number(),
                    workphone=random_phone_number(), email=random_email(10), email2=random_email(10),
                    email3=random_email(8), bday="30", bmonth="August", byear="1994", address=random_string("address", 10), address2="vampilov",
                    secondaryphone=random_phone_number(), notes=random_string("notes", 50))
            for i in range(5)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))