"""Selection sorting.

It improves on bubble sort by making only one exchange for every pass through
the list.

It looks for the largest value as it makes a pass and, after completing the
pass, places it in the proper location. But in the bubble sort, after the first
pass, the largest item is in the correct place.

On each pass, the largest remaining item is selected and then placed in its
proper location.

The selection sort makes the same number of comparisons as the bubble sort.
However, due to the reduction in the number of exchanges, the selection sort
typically executes faster in benchmark studies.
"""

def selection_sort(given_list):
    # Reverse traverse the list from n-1 to 0. This sorts the list from right
    # to left (larger number at the right and smaller number at the left).
    # Start the loop from len(given_list) - 1 to 0.
    for fill_slot in range(len(given_list) - 1, 0, -1):
        # The loop iterates from n-1 to 1.
        # Assume position of max value is at the first location, index 0.
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            # Update the pos_of_max value with the current value; if the
            # current value in the list is greater than the pos_of_max value.
            if given_list[location] > given_list[pos_of_max]:
                pos_of_max = location
        # Swap the value at the right side (fill_slot position) with the
        # pos_of_max value.
        temp = given_list[fill_slot]
        given_list[fill_slot] = given_list[pos_of_max]
        given_list[pos_of_max] = temp
        print(given_list, fill_slot)
    return given_list


if __name__ == '__main__':
    GIVEN_LIST = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(selection_sort(GIVEN_LIST))
