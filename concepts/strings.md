# Strings concepts and QA.

st = "This is dhanu and dhanu is learning python!"
st_numbers = '123456789'

1. What does it means for strings to be immutable in python?

   Once a string object has been created, it cannot be changed. Modifying that string creates a whole new object in memory. The concept is proved using id() function.

2. Does defining a string twice creates one or two objects in memory?

   It only creates one. This helps python to save memory when dealing with large strings.
   eg:
   ```
   animal = 'dog'
   pet = 'dog'
   print(id(animal))
   print(id(pet))
   ```

   both returns the same value.


3. Confirm that 2 strings have the same identity?

   ```
   st1 = "dhanu"
   st2 = "Dhanu"
   st3 = "dhanu"
   st4 = "dhanu1"
   st5 = "    This is dhanu.     "

   print(st1 == st3)
   ```

4. Count the total number of characters in a string?

   ```
   print(len(st)
   ```

5. Check if a string contains a specific substring?

   ```
   print(st1 in st)
   ```

6. Find the index of first occurrence of a substring in a string? If substring is "dhanu"

   ```
   print(st.find(st1))
   ```

7. Count the number of a specific character in a string?

   ```
   print(st.count('a'))
   ```

8. Check if a string contains only numbers?

    ```
    print(st_numbers.isnumeric())
    ```

9. Search a specific part of a string for a substring?

   ```
   st.index('and', 10, 25)
   ```

10. Check is each word in a substring begins with a capital letter?

    ```
    print(st.istitle())
    ```

11. Capitalize the first character of a string.

    ```
    print(st1.capitalize())
    ```

12. Check if a string is composed of all lower case characters?

    ```
    print(st1.islower())
    ```

13. Check if a string is all uppercase?

    ```
    st1.isupper()
    ```

14. Check if the first character in a string is lowercase?

    ```
    print(st1[0].islower())
    ```

15. Check if all the characters in a string conform to ASCII?

    ```
    print(st.isascii())
    ```

16. Conver string to uppercase or lower case?

    ```
    st1.upper()
    st1.lower()
    ```

17. Check if a string contains only character of the alphabet?

    ```
    print(st4.isalpha())
    ```

18. Replace all instances of a substring in a string?

    ```
    st.replace('dhanu', 'dhanu')
    ```

19. Return minimum character in a string?

    ```
    min(st1)
    ```

20. Remove whitespace from left, right or both sides of a string.

    ```
    st5.lstrip()
    st.rstrip()
    st.strip()
    ```

21. Check if a string begins with or ends with a specific character?

    ```
    st.startswith('This')
    st.endswith('!')
    ```

22. Convert first and last character of a string?

    ```
    st1[0].upper() + st[1:-1] + st[-1].upper()
    ```

23. Print every 2nd character in the given string?

    ```
    st[0:-1:2]
    ```

24. Split a string on a specific character?

    ```
    print(st.split('dhanu'))
    ```

25. When would you use splitlines()?

    ```
    st3 = "This is a python lesson.\nStudying everyday.\nAnd practising."
    st3.splitlines()
    ```

26. Join a list of strings into a single string, delimited by hyphens?

    ```
    print('-'.join(['a', 'b', 'c'])
    ```

27. What is an f-string and how do you use it?

    ```
    New in python 3.6, f-strings make string interpolation really easy. Using f-strings is similar to using format(). F-strings are denoted by an f before the opening quote.
    name = 'Chris'
    food = 'creme brulee'
    f'Hello. My name is {name} and I like {food}.'
    #=> 'Hello. My name is Chris and I like creme brulee'
    ```

28. Interpolate a variable into a string using format()?

    ```
    print('This is {}'.format(st1))
    ```

29. Can an integer be added to a string?

    ```
    NO
    st1 + 10 -> TypeError
    ```

30. Return the first matching substring in the given string?

    ```
    st.rfind('dhanu')
    ```

31. Reverse the string "hello world"

    ```
    ''.join(my_own_func_covert_str_to_list_and_reverse("hello world"))
    ```