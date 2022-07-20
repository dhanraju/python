"""
1. Write a Python program to print the following string in a specific format
(see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up\
above the world so high, Like a diamond in the sky. Twinkle, twinkle, little\
star, How I wonder what you are"

Output :
Twinkle, twinkle, little star,
        How I wonder what you are! 
                Up above the world so high,   		
                Like a diamond in the sky. 
Twinkle, twinkle, little star, 
        How I wonder what you are
"""

def prog001(input_string):
    # Convert input string to the given format.
    # Algorithm:
    # * Split the string into new lines when capital letters are found.
    # * Exclude character I; while splitting the string to new lines.
    # * Add 8 spaces at the beginning of the new line.
    # * Add 16 spaces at the beginning of the new line from line 3 to remaining
    #   lines.
    # * No spaces added to the line starts with Twinkle.
