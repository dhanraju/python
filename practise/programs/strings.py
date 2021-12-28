'''Strings demo.'''
print
pprint("***** Given Strings ****")
STR1 = "          3333333this is STR1 string333333          "
STR2 = "string2"
pprint("STR1 = '%s'" % STR1)
pprint("STR2 = '%s'" % STR2)

print
pprint("***** String Methods *****"
pprint("STR1.lower() = '%s'" % STR1.lower())
pprint("STR1.upper() = '%s'" % STR1.upper())
pprint("STR1.lstrip() = '%s'" % STR1.lstrip())
pprint("STR1.rstrip() = '%s'" % STR1.rstrip())
pprint("STR1.strip(\" 3\") = '%s'" % STR1.strip(" 3"))
pprint("STR1.swapcase() = '%s'" % STR1.swapcase())
pprint("\",\".join(STR2) = '%s'" % ",".join(STR2))
