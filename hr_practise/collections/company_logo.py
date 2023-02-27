"""Company Logo.

A newly opened multinational brand has decided to base their company logo on
the three most common characters in the company name. They are now trying out
various combinations of company names and logos based on this condition. Given
a string 's', which is the company name in lowercase letters, your task is to
find the top three most common characters in the string.

* Print the three most common characters along with their occurrence count.
* Sort in descending order of occurrence count.
* If the occurrence count is the same, sort the characters in alphabetical order.

For example, according to the conditions described above,
GOOGLE would have it's logo with the letters G, O, E.

Input: aabbbccde
Output:
b 3
a 2
c 2
"""
# from collections import Counter

def sort_char_occurrence_count(given_string):
    """Sort the given string in desc order based on number of occurrences."""
    string_dict = {}
    result_dict = {}
    # Create dictorinary with keys as letters and values as # of occurrences.
    for i in given_string:
        if i in string_dict.keys():
            string_dict[i] = string_dict[i]+1
        else:
            string_dict[i] = 1
    # string_dict = Counter(list(given_string))
    # Sort dictionary based on alphabetical order.
    myKeys = list(string_dict.keys())
    myKeys.sort()
    sorted_dict = {i: string_dict[i] for i in myKeys}
    # print(Counter(list(given_string)))
    # Sort in descending order based on # of occurrences.
    sorted_values = sorted(sorted_dict.items(), key = lambda value: value[1],
                           reverse=True)
    for i in range(3):
        print(sorted_values[i][0], sorted_values[i][1])
        result_dict[sorted_values[i][0]] = sorted_values[i][1]
    return result_dict


if __name__ == '__main__':
    s = input()
    sort_char_occurrence_count(s)