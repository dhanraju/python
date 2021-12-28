"""This module demonstrates sorting techniques."""

class SortingTechniques(object):
    """Sorting Techniques class."""
    def __init__(self):
        print("Constructor")

    @staticmethod
    def bubble_sort(list_obj):
        """Bubble sort technique."""
        for _ in range(len(list_obj)):
            for i in range(1, len(list_obj)):
                if list_obj[i] < list_obj[i-1]:
                    temp = list_obj[i]
                    list_obj[i] = list_obj[i-1]
                    list_obj[i-1] = temp
        return list_obj

    @classmethod
    def insertion_sort(cls, list_obj):
        """Insertion sort technique."""
        pass

    @classmethod
    def selection_sort(cls, list_obj):
        """Selection sort technique."""
        pass

    @classmethod
    def quick_sort(cls, list_obj):
        """Quick sort technique."""
        pass

    @classmethod
    def merge_sort(cls, list_obj):
        """Merge sort technique."""
        pass

    @classmethod
    def heap_sort(cls, list_obj):
        """Heap sort technique."""
        pass


def main():
    """Start of program."""
    sort_obj = SortingTechniques()
    list_obj = [5, 3, 6, 2, 4, 1]
    print("Given list : ", list_obj)
    print("Bubble sorted list : ", sort_obj.bubble_sort(list_obj))

if __name__ == '__main__':
    main()
