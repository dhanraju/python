"""Binary Search.

A binary search will start by examining the middle item. If that item is the
one we are searching for, we are done. If it is not, we can use the ordered
nature of the list to eliminate half of the remaining items. If the item we
are searching for is greater than the middle item, we know that the entire
lower half of the list as well as the middle item can be eliminated from
further consideration. The item, if it is in the list, must be in the upper
half. We can then repeat the process with the uppser half.
"""

def binary_search(given_list, item):
    first = 0
    last = len(given_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if given_list[midpoint] == item:
            found = True
        elif item < given_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return found


if __name__ == "__main__":
    GIVEN_LIST = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    ITEM1 = 3
    print(f'Is the item {ITEM1} present in the given list {GIVEN_LIST} ?',
        binary_search(GIVEN_LIST, ITEM1))

    ITEM2 = 13
    print(f'Is the item {ITEM2} present in the given list {GIVEN_LIST} ?',
        binary_search(GIVEN_LIST, ITEM2))
