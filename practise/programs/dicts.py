'''Dictionary demonstration.'''
print("***** Given Dictionaries ****")
DICT_OBJ1 = {
    'Name': 'Zara',
    'Age': 7,
    'Class': 'First'
}

DICT_OBJ2 = {
    'Name': 'Test',
    'Age': 3,
    'Class': 'Dev'
}

DICT_OBJ3 = {
    'Name': 'Zara',
    'Age': 7,
    'Class': 'First'
}

DICT_OBJ4 = {}

TUP_OBJ = ('Name', 'Age', 'Class')

print("***** Accessing Dictionary values *****")
print("DICT_OBJ1['Name'] = '%s'" % DICT_OBJ1['Name'])
print("DICT_OBJ1['Age'] = '%s'" % DICT_OBJ1['Age'])
print("DICT_OBJ1['Class'] = '%s'" % DICT_OBJ1['Class'])

print("***** Updating & Adding Dictionary elements *****")
DICT_OBJ1['Age'] = 8
DICT_OBJ1['School'] = 'DPS School'

print("DICT_OBJ1['Age'] = '%s'" % DICT_OBJ1['Age']
print("DICT_OBJ1['School'] = '%s'" % DICT_OBJ1['School']

print("***** Properties of Dictionary Keys *****")
print("* No duplicate key is allowed.")
print("* Strings, number or tuples can be used as keys. But ['key'] not allowed")


print("***** Build-in Functions *****")
print("cmp(DICT_OBJ1, DICT_OBJ3) = %s" % cmp(DICT_OBJ1, DICT_OBJ3))
print("len(DICT_OBJ1) = %s" % len(DICT_OBJ1))
print("str(DICT_OBJ1) = %s" % str(DICT_OBJ1))

print("***** Build-in Methods *****")
print("DICT_OBJ1.items = %s" % DICT_OBJ1.items)
print("DICT_OBJ1.values = %s" % DICT_OBJ1.values)
print("DICT_OBJ1.keys = %s" % DICT_OBJ1.keys)
print("DICT_OBJ1.has_key('Name') = %s" % DICT_OBJ1.has_key('Name'))
# print("DICT_OBJ4.copy(DICT_OBJ1)" % DICT_OBJ4.copy(DICT_OBJ1))
print("DICT_OBJ4.udpate(DICT_OBJ2) = %s" % DICT_OBJ4.update(DICT_OBJ2))
print("DICT_OBJ4.get('Name') = %s" % DICT_OBJ4.get('Name'))
print("DICT_OBJ4.setdefault('Height', None) = %s" % DICT_OBJ4.setdefault('Height', None))
# print("DICT_OBJ4.clear = %s" % DICT_OBJ4.clear)
print("DICT_OBJ4.fromkeys(TUP_OBJ) = %s" % DICT_OBJ4.fromkeys(TUP_OBJ, 10))


print("***** Deleting Dictionary elements *****")
# print("del DICT_OBJ4['Name'] = %s" % $(del DICT_OBJ4['Name']))
# print("DICT_OBJ4.clear() = %s" % DICT_OBJ4.clear())
# print("del DICT_OBJ4" % (del DICT_OBJ4))
