"""Hashing concept.

A hash table is a collection og items which are stored in such a way as to make
it easy to find them later. Each position of the hash table, often called a
slot, can hold an item and is named by an integer value starting at 0.

The mapping between an item and the slot where that item belongs in the hash
table is called the hash funtion.

The hash function will take any item in the collection and return an integer
in the range of slot names between 0 and m-1.

Assume that we have the set of integer items 54, 26, 93, 17, 77 and 31.
Our hash function, sometimes referred to as the "remainder method", simply
takes an item and divides it by the table size (for example 11), returning the
remainder as the hash value (h(item) = item % 11). Note that this remainder
method (modulo arithmetic) will typically be present in some form in all hash
functions, since the result must be in the range of slot names. And, the table
size is irrespective to the number of times.

The hast values for the given interger items are calculated as:
h(54) = 54 % 11 = 4
h(26) = 6
h(93) = 3
h(17) = 7
h(77) = 7
h(31) = 1
Once the hash values have been computed, we can insert each item into the hash
table at the designated position. But the problem in the above example is, for
the values 17 and 77, the hash values are same. This is referred to as a
"collison" also called as "clash".

For a given collection of items, a hash function that maps each items into a
unique slot is referred to as a "Perfect hash function".

There are a number of common ways to extend the simple remainder method.

The folding method for constructing hash functions begins by dividing the item
into equal size pieces (the last piece may not be of equal size). These pieces
are then added together to give the resulting hash value.

For example, if the item is a phone number 436-555-4601, then take the digits
and divide them into groups of 2 (43, 65, 55, 46, 01).
After the additon, 43+65+55+46+01 = 201. If we assume our hash table has 11
slots, then we need to perform extra step by dividing by 11 and keeping the
remainder. In this case 210%11 is 1, so the phone number 436-555-4601 hashes to
slot 1.

Some folding methods go one step further and reverse every other piece before
the addition. For example, 43+56+55+64+01 = 219 which gives 219%11 = 10

Another numerical technique for constructing a has function is called the 
"mid-square-method".

We first square the item, and then extract some portion of the resulting
digits. For example, if the item were 44, we would first compute 44^2 = 1936.
By extracting the middle two digits, 93, and performing the remainder step, we
get 5 (93%11).

----------- INCOMPLETE ----------------

"""