"""Is given string is a Palindrome.
Write a function that takes a string as a parameter and returns True if the
string is a palindrome, False otherwise. Remember that a string is a palindrome
if it is spelled the same both forward and backward. for example: radar is a
palindrome. for bonus points palindromes can also be phrases, but you need to
remove the spaces and punctuation before checking. for example: madam i’m adam
is a palindrome. Other fun palindromes include:
* kayak
* aibohphobia
* Live not on evil
* Reviled did I live, said I, as evil I did deliver
* Go hang a salami; I’m a lasagna hog.
* Able was I ere I saw Elba
* Kanakanak – a town in Alaska
* Wassamassaw – a town in South Dakota
"""
import string

def is_palindrome(given_string):
    """Checks the given string is palindrome or not."""
    # Convert the string to lower case, remove the punctuation and then remove
    # the spaces.
    filtered_string =  given_string.lower().translate(
        str.maketrans('', '', string.punctuation)).replace(' ', '')
    str_len = len(filtered_string)
    if str_len > 2:
        if filtered_string[0] is filtered_string[str_len-1]:
            return is_palindrome(filtered_string[1:(str_len-1)])
        return False
    return True

if __name__ == '__main__':
    ST1 = "kayak"
    ST2 = "aibohphobia"
    ST3 = "Live not on evil"
    ST4 = "Reviled did I live, said I, as evil I did deliver"
    ST5 = "Go hang a salami; I'm a lasagna hog."
    ST6 = "Able was I ere I saw Elba"
    ST7 = "Kanakanak"
    ST8 = "Wassamassaw"
    print(f'The given string {ST1} is palindrome?', is_palindrome(ST1))
    print(f'The given string {ST2} is palindrome?', is_palindrome(ST2))
    print(f'The given string {ST3} is palindrome?', is_palindrome(ST3))
    print(f'The given string {ST4} is palindrome?', is_palindrome(ST4))
    print(f'The given string {ST5} is palindrome?', is_palindrome(ST5))
    print(f'The given string {ST6} is palindrome?', is_palindrome(ST6))
    print(f'The given string {ST7} is palindrome?', is_palindrome(ST7))
    print(f'The given string {ST8} is palindrome?', is_palindrome(ST8))
