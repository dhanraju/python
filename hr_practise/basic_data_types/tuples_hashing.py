"""Hashing problem."""

def get_hash_value(n, interger_list):
    hash_value = hash(interger_list)
    return hash_value


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(get_hash_value(n, tuple(integer_list)))