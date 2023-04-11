"""Binary search in recursive way."""
def binary_search_recursive(given_list, item):
    if len(given_list) == 0:
        return False
    else:
        midpoint = len(given_list) // 2
        if given_list[midpoint] == item:
            return True
        elif item < given_list[midpoint]:
            return binary_search_recursive(given_list[:midpoint], item)
        else:
            return binary_search_recursive(given_list[midpoint + 1:], item)


if __name__ == "__main__":
    GIVEN_LIST = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    ITEM1 = 3
    print(f'Is the item {ITEM1} present in the given list {GIVEN_LIST} ?',
        binary_search_recursive(GIVEN_LIST, ITEM1))

    ITEM2 = 13
    print(f'Is the item {ITEM2} present in the given list {GIVEN_LIST} ?',
        binary_search_recursive(GIVEN_LIST, ITEM2))
