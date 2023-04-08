"""Draw a spiral recursively using turtle module."""
import turtle


class DrawSpiral:
    """Draw spiral."""
    def __init__(self):
        # Initialize turtle object.
        self.my_turtle = turtle.Turtle()
        # Create a window for itself to draw in.
        self.my_win = turtle.Screen()

    def draw_spiral(self, line_len):
        """Draw spiral recursively."""
        # If the length of the line is greater than zero, draw forward by
        # length of line and then trun 90 degrees. Now reduce the length
        # by 5 and perform recrusively.
        if line_len > 0:
            self.my_turtle.forward(line_len)
            self.my_turtle.right(90)
            self.draw_spiral(line_len - 5)

    def __exit__(self):
        """Exit windown on click."""
        self.my_win.exitonclick()


if __name__ == "__main__":
    draw_spiral_obj = DrawSpiral()
    draw_spiral_obj.draw_spiral(500)
    draw_spiral_obj.__exit__()
