'''Create a data structure as follows:

variable = {
    'Date' = [],
    'VisitedPlaces' = [],
    'CreditcardUsed' = [],
    'TimeSpent' = []
}

Example usage:
The data structure holds the details of a person on "the date that the person
visited a place, used credit card in that place and the amount time the person
spent in that place.
Person1 = [
    ['Jan 01 2016', 'New York', 'Bank X', '6 hours'],
    ['Jan 30 2016', 'San Francisco', 'Bank Y', '3 hours'],
    ['Dec 01 2017', 'Tahoe', 'Bank Z', '12 hours']
]
Person2 = [
    ['Feb 10 2016', 'Delhi', 'Bank I', '6 hours'],
    ['Feb 20 2016', 'Agra', 'Bank J', '10 hours'],
]
'''

import os

C_DIR = os.getcwd()
DATA_STRUCT_PATH = '%s/data_struct.config' % C_DIR


#pylint: disable=too-few-public-methods
class _PersonData(object):
    def __init__(self, name):
        # Initialize data.
        self.name = name
        self.date = []
        self.place = []
        self.bank_name = []
        self.time_spent = []
#pylint: enable=too-few-public-methods

# Create a dictionary called DATA_BASE using list comprehension technique.
with open(DATA_STRUCT_PATH) as fp:
	  #pylint: disable=eval-used
    PERSONS = list(eval(fp.read()))
    #pylint: enable=eval-used

DATA_BASE = {person: _PersonData(person) for person in PERSONS}

# The above logic can be directly implemented as below.
'''DATA_BASE = {
    'personA': _PersonData('personA'),
    'personB': _PersonData('personB'),
    'personC': _PersonData('personC'),
    'personD': _PersonData('personD'),
    'personE': _PersonData('personE'),
    'personF': _PersonData('personF'),
    'personG': _PersonData('personG'),
    'personH': _PersonData('personH'),
    'personI': _PersonData('personI'),
    'personJ': _PersonData('personJ'),
}'''


if __name__ == '__main__':
    # date = raw_input('Date you visited the place: ')
    DATA = [
        ['personA', 'Jan 01 2016', 'New York', 'Bank X', '6 hours'],
        ['personB', 'Jan 02 2016', 'New York', 'Bank X', '6 hours'],
        ['personA', 'Jan 03 2016', 'Texas', 'Bank Y', '6 hours'],
        ['personC', 'Jan 04 2016', 'New York', 'Bank X', '6 hours'],
        ['personD', 'Jan 05 2016', 'New York', 'Bank X', '6 hours'],
        ['personB', 'Jan 06 2016', 'Texas', 'Bank X', '6 hours'],
        ['personA', 'Jan 07 2016', 'New York', 'Bank Y', '6 hours'],
        ['personA', 'Jan 08 2016', 'SFO', 'Bank Z', '6 hours'],
        ['personE', 'Jan 09 2016', 'New York', 'Bank Z', '6 hours'],
        ['personF', 'Jan 01 2016', 'New York', 'Bank X', '6 hours'],
        ['personG', 'Jan 02 2016', 'New York', 'Bank X', '6 hours'],
        ['personH', 'Jan 03 2016', 'New York', 'Bank X', '6 hours'],
        ['personI', 'Jan 04 2016', 'New York', 'Bank X', '6 hours'],
        ['personJ', 'Jan 05 2016', 'New York', 'Bank X', '6 hours'],
        ['personI', 'Jan 06 2016', 'Texas', 'Bank Y', '6 hours'],
        ['personI', 'Jan 07 2016', 'SFO', 'Bank Z', '6 hours'],
    ]

    #pylint: disable=consider-using-enumerate
    for i in range(len((DATA))):
        # print(DATA[i][0])
        for value in DATA_BASE.keys():
            if DATA[i][0] == value:
                # print(DATA_BASE[value].name
                DATA_BASE[value].date.append(DATA[i][1])
                DATA_BASE[value].place.append(DATA[i][2])
                DATA_BASE[value].bank_name.append(DATA[i][3])
                DATA_BASE[value].time_spent.append(DATA[i][4])
    #pylint: enable=consider-using-enumerate
    print("\n\n\n\n\n")
    for value in DATA_BASE.keys():
        print("***** %s Details *****" % value)
        print(DATA_BASE[value].date)
        print(DATA_BASE[value].place)
        print(DATA_BASE[value].bank_name)
        print(DATA_BASE[value].time_spent)
        print("**********************")
