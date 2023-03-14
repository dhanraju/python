"""A recursive implementaion of a function that draws a a ruler.

Draw the markings of a typical ruler. For each inch, we place a tick with a
numeric label. We denote the length of the tick designating a whole inch as the
MajorTickLength. Between the marks for whole inches, the ruler contains a
series of MinorTicks, placed at intervals of 1/2 inch, 1/4 inch and so on.
As the size of the interval decreases by half, the tick length decreases
by one.
"""

class EnglishRuler:
    """Draw the markings of a typical ruler."""

    def __init__(self, num_inches, major_length):
        self.num_inches = num_inches
        self.major_length = major_length

    def draw_line(self, tick_length, tick_label=' '):
        """Draw one line with given tick length (follwed by optional label)."""
        line = '-' * tick_length
        if tick_length:
            line += ' ' + tick_label
        print(line)

    def draw_interval(self, center_length):
        """Draw tick interval based upon a central tick length."""
        if center_length > 0:                      # Stop when len drops to 0
            self.draw_interval(center_length - 1)  # recursively draw top ticks
            self.draw_line(center_length)          # draw center tick
            self.draw_interval(center_length - 1)  # recus'ly draw bottom ticks

    def draw_ruler(num_inches, major_length):
        """Draw English ruler with given num of inches, major tick length."""
        draw.line(major_length, '0')         # draw inch 0 line
        for j in range(1, 1+num_inches):
            draw_interval(major_length-1)    # draw interior ticks for inch
            draw_line(major_length, str(j))  # draw inch j line and label


if __name__ == '__main__':
    english_ruler = EnglishRuler(5, 10)
    english_ruler.draw_interval(5)