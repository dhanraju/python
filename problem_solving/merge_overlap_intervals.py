"""Merge overlapping intervals problem.

You have an array (list) of interval pairs as input where each interval has
a start and end timestamp, sorted by starting timestamps. Merge the
overlapping intervals and return a new output array.
"""

def merge_overlap_intervals(arr):
    """Merges the overlapping intervals in the given array."""
    overlap_arr = []
    overlap_arr = arr[0]
    for i in range(1, len(arr)):
        if arr[i][0] < overlap_arr[0] :
            overlap_arr[0] = arr[i][0]
        if arr[i][1] > overlap_arr[1]:
            overlap_arr[1] = arr[i][1]
    return overlap_arr


if __name__ == "__main__":
    arr = [[1, 5], [3, 7], [4, 6], [6, 8]]
    print(merge_overlap_intervals(arr))