"""Reverse an integer."""

def reverse_int(num):
    '''Reverses the given integer value.'''
    st=''
    quotient = num
    remainder = 0
    print(quotient)
    print(int(quotient/10))
    while quotient >= 10:
        remainder = quotient%10
        quotient = int(quotient/10)
        st = st+str(remainder)
    st = st+str(quotient)
    return int(st)


if __name__ == '__main__':
    num = 4619
    print('Reverse of %d is %d' % (num, reverse_int(num)))