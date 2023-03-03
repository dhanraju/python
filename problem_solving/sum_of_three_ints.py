"""Determine if the sum of three integers is equal to the given value.

Given an array of integers and a value, determine if there are any three
integers in the array whose sum equals the given value.
"""

def sum_of_three_ints(arr, value):
    """Return an array of values that sums up the given value."""
    result_arr = []
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if arr[i]+arr[j]+arr[k] == value:
                    result_arr.append([arr[i], arr[j], arr[k]])
    return result_arr


if __name__ == "__main__":
    arr = [5, 6, 9, 8, 3, 2, 7, 4, 1]
    value = 20
    print(sum_of_three_ints(arr, value))