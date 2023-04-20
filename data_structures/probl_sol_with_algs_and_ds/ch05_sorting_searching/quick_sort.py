"""Quick sorting.

It uses divide and conquer to gain the same advantages as the merge sort, while
not using additional storage. As a trade-off, however it is possible that the
list may not be divided in half. When this happens, the perfomance will be
diminished.

It selects a value, which is called the pivot value. Although there are many
different ways to choose the pivot value, we simply use the first item in the
list.

The role of the pivot is to assit with splitting the list. The actual position
where the pivot values belongs in the final sorted list, commonly called the
split point, will be used to divide the list for subsequent calls to the quick
sort.

It uses two positional markers, called left_mark and right_mark - at the
beginning and end of the remaining items in the list. The goal of using these
markers is to move items that are on the wrong side with respect to the pivot
value while also converging on the split point. This process is called
partition.

We begin by incrementing left_mark until we locate a value that is greater than
the pivot value. We then decrementing right_mark until we find a value that is
less than the pivot value.

At this point we have discovered two items that are out of place with respect
to the eventual split point.

Now we can exchange these two items and then repeat the process again.

At the point where right_mark becomes less than left_mark, we stop. The
position of right_mark is now the split point. The pivot value can be
exchanged with the contents of the split point and the pivot value is now in place.

In addition, all the items to the left of the split point are less than the
pivot value, and all the items to the right of the split pint are greater
than the pivot values. The list van now be divided at the split point and the
quick sort can be invoked recursively on the two halves.

The quick_sort functions invokes a recursive function, quick_sort_helper.
quick_sort_helper begins with the same base case as the merge sort. If the
lenght of the list is less than or equal to one, it is already sorted. If it
is greater, then it can be partitioned and recursively sorted.
"""

def quick_sort(given_list):
    print('Given list is: ', given_list)
    quick_sort_helper(given_list, 0, len(given_list) - 1)
    return given_list

def quick_sort_helper(given_list, first, last):
    # Perform divide and conquer.
    if first < last:
        # Partition the given list.
        split_point = partition(given_list, first, last)
        # Perform divide and conquer recursively on partitioned lists.
        quick_sort_helper(given_list, first, split_point - 1)
        quick_sort_helper(given_list, split_point + 1, last)

def partition(given_list, first, last):
    pivot_value = given_list[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and given_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while given_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = given_list[left_mark]
            given_list[left_mark] = given_list[right_mark]
            given_list[right_mark] = temp
    temp = given_list[first]
    given_list[first] = given_list[right_mark]
    given_list[right_mark] = temp
    return right_mark


if __name__ == '__main__':
    GIVEN_LIST = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(quick_sort(GIVEN_LIST))
