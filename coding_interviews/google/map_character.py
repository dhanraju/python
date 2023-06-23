"""
Find if there is a one to one mapping possible for every character of str1 to every character of str2 and. And all occurrences of every character in ‘str1’ map to same character in ‘str2’ vice vera.


Scenario 1:
str1: adba
str2: cbfc
return true

Scenario 2:
str1: adba
str2: cbfv
return false
"""

def map_character(str1, str2) -> bool:
    """Verifies str1 characters mapped with str2 and return the result."""
    dict1 = {}
    dict2 = {}
    # Create a dynamic map for the characters in str1 with respect to str2
    # and viceversa.
    # Use dictionaries for each string (dict1 for str1 and dict2 for str2),
    # Traverse through the string char by char, update dictionary keys and
    # values with str1 and str2 
    # for example,
    # dict1 { 
    #   key0=str1[0]: value0=str2[0],
    #   key1=str1[1]: value1=str2[1],
    #   and so on until the length of the string.
    # }
    # And same for dict2
    # dict2 { 
    #   key0=str2[0]: value0=str1[0],
    #   key1=str2[1]: value1=str1[1],
    #   and so on until the length of the string.
    # }
    # The resultant dictionaries looks likes this:
    # dict1 = {'a': 'c', 'd': 'b', 'b': 'f'} and
    # dict2 = {'c': 'a', 'b': 'd', 'f': 'b'}
    # Now compare the key:value pair of dict1 with key:value pair of dict2.
    # Here, the dict1.key == dict2[key] # accessing value and
    # dict2.key == dict1[key]
    for i in range(len(str1)):
        if str1[i] not in dict1.keys():
            dict1[str1[i]] = str2[i]
        if str2[i] not in dict2.keys():
            dict2[str2[i]] = str1[i]
    print(dict1)
    print(dict2)
    # First check, if both strings are mapped correctly, then their length
    # should be equal.
    if len(dict1) != len(dict2):
        return False
    # Now verify key:value pairs.
    for i in dict1.keys():
        print(i, dict2[dict1[i]])
        if i != dict2[dict1[i]]:
            return False
    for i in dict2.keys():
        print(i, dict1[dict2[i]])
        if i != dict1[dict2[i]]:
            return False
    return True


if __name__ == "__main__":
    str1 = "adba"
    str2 = "cbfc"
    print(map_character(str1, str2))
