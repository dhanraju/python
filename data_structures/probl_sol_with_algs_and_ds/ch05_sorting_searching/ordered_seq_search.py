"""Ordered Sequential Search.

Assume that the list of items was constructed so that the items were in
ascending order, from low to high. If the item we are looking for is present
in the list, the chance of it being in anyone of the n positions is still the
same as before.
"""

def ordered_sequential_search(given_list, item):
    """Ordered sequential search."""
    pos = 0
    found = False
    stop = False
    while pos < len(given_list) and not found and not stop:
        if given_list[pos] == item:
            found = True
        elif given_list[pos] > item:
            stop = True
        else:
            pos = pos + 1

    return found


if __name__ == "__main__":
    GIVEN_LIST = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    ITEM1 = 3
    print(f'Is the item {ITEM1} present in the given list {GIVEN_LIST} ?',
        ordered_sequential_search(GIVEN_LIST, ITEM1))

    ITEM2 = 13
    print(f'Is the item {ITEM2} present in the given list {GIVEN_LIST} ?',
        ordered_sequential_search(GIVEN_LIST, ITEM2))
