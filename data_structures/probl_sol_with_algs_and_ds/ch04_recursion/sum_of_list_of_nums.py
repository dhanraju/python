"""Calculating the sum of a list of numbers using recursion."""

def list_sum(num_list):
    """Calculates sum of numbers in a list."""
    the_sum = 0
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])


if __name__ == '__main__':
    GIVEN_NUM_LIST = [1, 3, 5, 7, 9]
    print(f'The sum of given list {GIVEN_NUM_LIST} is',
        list_sum(GIVEN_NUM_LIST))