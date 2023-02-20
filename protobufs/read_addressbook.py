"""Reads the data stored in addressbook format."""

import addressbook_pb2
import sys


def ListPeople(address_book):
    '''Iterates through all people in the AddressBook and prints info.'''
    for person in address_book.people:
        print("Person ID: ", person.id)
        print("Name: ", person.name)
        if person.HasField('email'):
            print("E-mail address: ", person.email)

        for phone_number in person.phones:
            if phone_number.type == addressbook_pb2.Person.PhoneType.MOBILE:
                print("Mobile phone #: ", phone_number.number)
            elif phone_number.type == addressbook_pb2.Person.PhoneType.HOME:
                print("Home phone #: ", phone_number.number)
            elif phone_number.type == addressbook_pb2.Person.PhoneType.WORK:
                print("Work phone #: ", phone_number.number)
            else:
                print("Type of phone %s is : UNKNOWN" % phone_number.type)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ", sys.argv[0], "ADDRESS_BOOK_FILE")
        sys.exit(1)

    address_book = addressbook_pb2.AddressBook()

    # Read the existing address book.
    f = open(sys.argv[1], "rb")
    address_book.ParseFromString(f.read())
    f.close()

    ListPeople(address_book)