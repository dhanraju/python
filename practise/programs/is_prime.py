'''Is Prime NUMBER.'''
#!/usr/bin/python

def is_prime_num(num):
    '''Is prime NUMBER.'''
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                print("The given NUMBER is divisible by '%d' and hence is not a\
 prime NUMBER" % i)
                return
    print("The given NUMBER '%d' is a prime NUMBER" % num)


if __name__ == '__main__':
    NUMBER = int(raw_input("Enter a NUMBER:"))
    is_prime_num(NUMBER)
