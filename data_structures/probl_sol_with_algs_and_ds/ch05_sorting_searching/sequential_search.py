"""Sequential Search.

When data items is stored in a collection such as a list, then they have a
linear or sequential relationship. Each item is accessed through its positional
values in a sequential order. We simply move from item to item, following the
underlying sequential ordering until either the item founds or runs out of
items.
"""
def sequential_search(given_list, item):
    """Sequential search."""
    pos = 0
    found = False

    while pos < len(given_list) and not found:
        if given_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


if __name__ == "__main__":
    GIVEN_LIST = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    ITEM1 = 3
    print(f'Is the item {ITEM1} present in list {GIVEN_LIST} ?',
        sequential_search(GIVEN_LIST, ITEM1))

    ITEM2 = 13
    print(f'Is the item {ITEM2} present in list {GIVEN_LIST} ?',
        sequential_search(GIVEN_LIST, ITEM2))
