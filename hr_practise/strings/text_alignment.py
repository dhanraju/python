"""
Generate the HackerRank Logo of variable thickness.

Input Format: A single line containing the thickness value for th elogo.
Constraints: The thickness must be an odd number 0 < thickness < 50
Output Format: Output the desired logo.

Sample Input:
5

Sample Output:
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
"""


def text_alignment(thickness, c):
    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print(
            (c*thickness).center(thickness*2) +
            (c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    #Bottom Pillars
    for i in range(thickness+1):
        print(
            (c*thickness).center(thickness*2) +
            (c*thickness).center(thickness*6))

    #Bottom Cone
    for i in range(thickness):
        print(
            ((c*(thickness-i-1)).rjust(thickness) +
            c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

if __name__ == '__main__':
    THICKNESS = 5 #This must be an odd number
    CH = 'H'
    text_alignment(THICKNESS, CH)
