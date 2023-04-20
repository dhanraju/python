"""Merge sorting.

It uses divide and conquer strategy. It is a recursive algorithm that
continually splits a list in half. If the list is empty or has one item, it is
sorted by definition. If the list has more than one item, we split the list and
recursively invoke a merge sort on both halves.

Once the two halves are sorted, the fundamental operation called a "merge" is
performed. Merging is the process of taking two smaller sorted lists and
combining them together into a single, sorted new list.
"""

def merge_sort(given_list):
    print('Splitting list: ', given_list)
    if len(given_list) > 1:
        mid = len(given_list) // 2
        left_half = given_list[:mid]
        right_half = given_list[mid:]

        # Call recursively on both halves.
        merge_sort(left_half)
        merge_sort(right_half)

        # Sort the sub lists.
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                given_list[k] = left_half[i]
                i = i + 1
            else:
                given_list[k] = right_half[j]
                j = j + 1
            k = k + 1
        
        # Merge all the sub lists.
        # Merge all the left half of the sublists.
        while i < len(left_half):
            given_list[k] = left_half[i]
            i = i + 1
            k = k + 1
        # Merge all the right half of the sublists.
        while j < len(right_half):
            given_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    print('Merged list: ', given_list)
    return given_list


if __name__ == '__main__':
    GIVEN_LIST = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(merge_sort(GIVEN_LIST))
