"""This module prints fibonacci series of a number."""
#!/usr/bin/python

def fibonacci_series(num):
    """Returns a list contains fibonacci series of a number."""
    if num == 0:
        return 0
    list_obj = [0, 1]
    for _ in range(1, num):
        j = list_obj[-1] + list_obj[-2]
        list_obj.append(j)
    return list_obj


def main():
    """Start of the program."""
    print("Enter a number to get fibonacci series:")
    num = int(raw_input())
    print(fibonacci_series(num))

if __name__ == '__main__':
    main()
