"""Insertion sorting.

It always maintains a sorted sublist in the lower portions of the list.
Each new item is then "inserted" back into the previous sublist such that
the sorted sublist is one item larger.

Assume that a list with one item (at position 0) is already sorted. On each
pass, one for each item 1 through n-1, the current item is checked against
those in the already sorted sublist. In the sorted sublist, we shift those
items that are greater to the right. When we reach a smaller item or the end
of the sublist, the current item can be inserted.

The iteration starts at position 1 and moves through position n-1, as there are
the items that need to be inserted back into the sublists.
"""

def insertion_sort(given_list):
    # Traverse the list from position 1 to n-1.
    for index in range(1, len(given_list)):
        current_value = given_list[index]
        position = index
        # Check if the value at given index is less than the previous value.
        while (position > 0) and (given_list[position - 1] > current_value):
            given_list[position] = given_list[position - 1]
            position = position - 1
        given_list[position] = current_value
        print(given_list, index)
    return given_list


if __name__ == '__main__':
    GIVEN_LIST = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(insertion_sort(GIVEN_LIST))
