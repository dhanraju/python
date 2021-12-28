'''Euclid's Division Lemma Theorem:
Given positive integers a and b, there exist unique pair of integers
q and r satisfying a = bq + r, 0 <= r < b.
'''

# METHOD 1: Traditional way of finding HCF of two numbers.
def factorsOfValue(val):
    factors = []
    for i in range(1, val):
        if val%i == 0:
            factors.append(i)
    factors.append(val)
    # print(factors)
    return factors

def getCommonFactors(list_a, list_b):
    common_factors = []
    for i in range(len(list_a)):
        for j in range(len(list_b)):
            if list_a[i] == list_b[j]:
                common_factors.append(list_a[i])
    return common_factors

def getHCF(val_a, val_b):
    val_a_factors = factorsOfValue(val_a)
    val_b_factors = factorsOfValue(val_b)
    # print('val_a_factors = ', val_a_factors)
    # print('val_b_factors = ', val_b_factors)
    common_factors = getCommonFactors(val_a_factors, val_b_factors)
    if len(common_factors) == 0:
        print('There is no HCF of numbers: ', val_a, val_b)
        return
    return common_factors[-1]


# METHOD 2: Using Euclid's Division Lemma algorithm, find HCF of two numbers.
def euclidDivision(val_a, val_b):
    if val_a > val_b:
        large_num = val_a
        small_num = val_b
    else:
        large_num = val_b
        small_num = val_a
    remainder = 1
    quotient = 1
    temp = 0
    # Initial check: Is large number divisible by small number,
    # return small numer as HCF
    if large_num%small_num == 0:
        # print('Initial check passed!')
        return small_num
    while remainder != 0:
        # print('***', large_num, small_num, remainder, quotient)
        quotient = large_num%small_num
        remainder = large_num/small_num
        if quotient == 0:
            return temp
        else:
            temp = quotient
        large_num = small_num
        small_num = quotient
    return temp


''' Problem: Using Euclid's lemma, get HCF of two numbers.'''
if __name__ == '__main__':
    print('***** Euclid\'s Division Lemma Algorithm *****')
    print('HCF (100, 60) = ', euclidDivision(60, 100))
    print('HCF (90, 30) = ', euclidDivision(90, 30))
    print('HCF (50, 70) = ', euclidDivision(50, 70))
    print('HCF (96, 72) = ', euclidDivision(96, 72))
    print('HCF (300, 550) = ', euclidDivision(300, 550))
    print('HCF (1860, 2015) = ', euclidDivision(1860, 2015))

    print('***** Traditional way of finding HCF of two numbers. *****')
    print('HCF (100, 60) = ', getHCF(60, 100))
    print('HCF (90, 30) = ', getHCF(90, 30))
    print('HCF (50, 70) = ', getHCF(50, 70))
    print('HCF (96, 72) = ', getHCF(96, 72))
    print('HCF (300, 550) = ', getHCF(300, 550))
    print('HCF (1860, 2015) = ', getHCF(1860, 2015))
