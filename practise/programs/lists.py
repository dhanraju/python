'''Lists demonstration.'''
print("***** List operations *****")
LIST_OBJ1 = [1, 2, 1, 2, 3]
LIST_OBJ1_DUP = [1, 2, 1, 2, 3]
LIST_OBJ2 = [4, 5, 6, 7, 8]
LIST_OBJ3 = [3, 2, 1, 2, 1]
LIST_OBJ4 = [0, 9, 8, 7, 6]
TUPLE_OBJ = ('a', 'b', 'c', 'd', 'e')

print
print("***** Given lists *****")
print("LIST_OBJ1 = ", LIST_OBJ1)
print("LIST_OBJ2 = ", LIST_OBJ2)
print("LIST_OBJ3 = ", LIST_OBJ3)
print("LIST_OBJ4 = ", LIST_OBJ4)
print("LIST_OBJ1_DUP = ", LIST_OBJ1_DUP)

print
print("***** List Indexing *****")
print("LIST_OBJ1[0] = ", LIST_OBJ1[0])
print("LIST_OBJ1[4] = ", LIST_OBJ1[4])
print("LIST_OBJ1[-1] = ", LIST_OBJ1[-1])
print("LIST_OBJ1[-4] = ", LIST_OBJ1[-4])

print
print("***** List slicing *****")
print("LIST_OBJ1[:] = ", LIST_OBJ1[1:])
print("LIST_OBJ1[:3] = ", LIST_OBJ1[:3])
print("LIST_OBJ1[2:] = ", LIST_OBJ1[2:])
print("LIST_OBJ1[2:4] = ", LIST_OBJ1[2:4])

print
print("***** List Methods *****")
print("LIST_OBJ1.count(1) = ", LIST_OBJ1.count(1))
print("LIST_OBJ1.index(3) = ", LIST_OBJ1.index(3))
LIST_OBJ2.append(9)
print("LIST_OBJ2.append(9) = ", LIST_OBJ2)
LIST_OBJ2.reverse()
print("LIST_OBJ2.reverse() = ", LIST_OBJ2)
LIST_OBJ2.sort()
print("LIST_OBJ2.sort() = ", LIST_OBJ2)
LIST_OBJ2.extend(TUPLE_OBJ)
print("LIST_OBJ2.extend(TUPLE_OBJ) = ", LIST_OBJ2)
LIST_OBJ2.remove(8)
print("LIST_OBJ2.remove(8) = ", LIST_OBJ2)
LIST_OBJ2.pop(-4)
print("LIST_OBJ2.pop(-4) = ", LIST_OBJ2)
LIST_OBJ2.sort()
print("LIST_OBJ2.sort() = ", LIST_OBJ2)

print
print("***** List Functions *****")
print("len(LIST_OBJ4) = ", len(LIST_OBJ4))
print("max(LIST_OBJ4) = ", max(LIST_OBJ4))
print("min(LIST_OBJ4) = ", min(LIST_OBJ4))
print("cmp(LIST_OBJ1, LIST_OBJ1_DUP) = ", cmp(LIST_OBJ1, LIST_OBJ1_DUP))
print("list(TUPLE_OBJ) = ", list(TUPLE_OBJ))

print
print("***** List Operations *****")
print("LIST_OBJ1 '+' LIST_OBJ2 = ", (LIST_OBJ1+LIST_OBJ2))
print("LIST_OBJ1 '*' 2 = ", (LIST_OBJ1*2))

#pylint: disable=pointless-string-statement
""" ---------------- OUTPUT -----------------
***** List operations *****

***** Given lists *****
LIST_OBJ1 =  [1, 2, 1, 2, 3]
LIST_OBJ2 =  [4, 5, 6, 7, 8]
LIST_OBJ3 =  [3, 2, 1, 2, 1]
LIST_OBJ4 =  [0, 9, 8, 7, 6]
LIST_OBJ1_DUP =  [1, 2, 1, 2, 3]

***** List Indexing *****
LIST_OBJ1[0] =  1
LIST_OBJ1[4] =  3
LIST_OBJ1[-1] =  3
LIST_OBJ1[-4] =  2

***** List slicing *****
LIST_OBJ1[:] =  [2, 1, 2, 3]
LIST_OBJ1[:3] =  [1, 2, 1]
LIST_OBJ1[2:] =  [1, 2, 3]
LIST_OBJ1[2:4] =  [1, 2]

***** List Methods *****
LIST_OBJ1.count(1) =  2
LIST_OBJ1.index(3) =  4
LIST_OBJ2.append(9) =  [4, 5, 6, 7, 8, 9]
LIST_OBJ2.reverse() =  [9, 8, 7, 6, 5, 4]
LIST_OBJ2.sort() =  [4, 5, 6, 7, 8, 9]
LIST_OBJ2.extend(TUPLE_OBJ) =  [4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
LIST_OBJ2.remove(8) =  [4, 5, 6, 7, 9, 'a', 'b', 'c', 'd', 'e']
LIST_OBJ2.pop(-4) =  [4, 5, 6, 7, 9, 'a', 'c', 'd', 'e']
LIST_OBJ2.sort() =  [4, 5, 6, 7, 9, 'a', 'c', 'd', 'e']

***** List Functions *****
len(LIST_OBJ4) =  5
max(LIST_OBJ4) =  9
min(LIST_OBJ4) =  0
cmp(LIST_OBJ1, LIST_OBJ1_DUP) =  0
list(TUPLE_OBJ) =  ['a', 'b', 'c', 'd', 'e']

***** List Operations *****
LIST_OBJ1 '+' LIST_OBJ2 =  [1, 2, 1, 2, 3, 4, 5, 6, 7, 9, 'a', 'c', 'd', 'e']
LIST_OBJ1 '*' 2 =  [1, 2, 1, 2, 3, 1, 2, 1, 2, 3]

"""
#pylint: enable=pointless-string-statement
