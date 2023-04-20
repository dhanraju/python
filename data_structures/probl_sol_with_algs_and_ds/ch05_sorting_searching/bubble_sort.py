"""Bubble sort.

It compares adjacent items and exchanges those that are out of order.

Each pass through the list; places the next largest value in its proper place.
In essence, each item "bubbles" up to the location where it belongs.

If there are "n" items in the list, then there are "n-1" pairs of items that
need to be compared on the first pass.
"""

def bubble_sort(given_list):
    """Bubble sort algorithm."""
    pass_num = 0
    # Pass through all the elements in the list.
    for _ in range(len(given_list)-1):
        # Compare adj elements from the beginning.
        # Then leave the last sorted element for comparison.
        for i in range(len(given_list)-1-pass_num):
            if given_list[i] > given_list[i+1]:
                # Swap the elements.
                temp = given_list[i]
                given_list[i] = given_list[i+1]
                given_list[i+1] = temp
                print(given_list)
        # The largest value should be placed in the right place. So ignore the
        # sorted values that are placed at the end of the list for traversal.
        pass_num = pass_num + 1  # Leave the last sorted element for comparison
    return given_list

if __name__ == '__main__':
    GIVEN_LIST = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(f'Sorted list of given list {GIVEN_LIST} is ',
        bubble_sort(GIVEN_LIST))
