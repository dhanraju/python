"""Sierpinski Triangle.

Another fractal that exhibits the property of similarity is the Sierpinski
triangle. It illustrates a three-way recursive algorithm.

The procedure for drawing a Sierpinski triangle by hand is simple. Start with
a single large triangle. Dividide this large triangle into four new triangles
by connecting the midpoint of each side. Ignoring the middle triangle that you
just created, apply the same procedure to each of the three corner triangles.
Each time you create a new set of triangles, you recursively apply this
procedure to the three smaller corner triangles.

You can continue to apply this procedure indefinitely if you have a sharp
enough pencil. The base case is set arbitrarily as the number of times we want
to divide the triangle into pieces. Sometimes we call this number the "degree"
of the fractal. When we reach a degree of 0, we stop making recursive calls.
"""

import turtle


class SierpinskiTriangle:
    """Construct Sierpinski triangle."""
    def __init__(self):
        self.my_turtle = turtle.Turtle()
        self.my_win = turtle.Screen()

    def sierpinski(self, points, degree):
        """Draw sierpinski triangle."""
        color_map = [
            'blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
        self.draw_triangle(points, color_map[degree])
        if degree > 0:
            self.sierpinski(
                [points[0],
                 self.get_mid(points[0], points[1]),
                 self.get_mid(points[0], points[2])],
                degree - 1)
            self.sierpinski(
                [points[1],
                 self.get_mid(points[0], points[1]),
                 self.get_mid(points[0], points[2])],
                degree - 1)
            self.sierpinski(
                [points[2],
                 self.get_mid(points[2], points[1]),
                 self.get_mid(points[0], points[2])],
                degree - 1)

    def draw_triangle(self, points, color):
        """Draw triangle and fill color."""
        self.my_turtle.fillcolor(color)
        self.my_turtle.up()
        self.my_turtle.goto(points[0][0], points[0][1])
        self.my_turtle.down()
        self.my_turtle.begin_fill()
        self.my_turtle.goto(points[1][0], points[1][1])
        self.my_turtle.goto(points[2][0], points[2][1])
        self.my_turtle.goto(points[0][0], points[0][1])
        self.my_turtle.end_fill()

    def get_mid(self, p1, p2):
        """Return mid point of the side of the triangle."""
        return ( (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 )

    def __exit__(self):
        """Exit the window on click."""
        self.my_win.exitonclick()


if __name__ == '__main__':
    POINTS = [ [-200, -100], [0, 200], [200, -100] ]
    DEGREE = 4
    sierpinski_triangle_obj = SierpinskiTriangle()
    sierpinski_triangle_obj.sierpinski(POINTS, DEGREE)
    sierpinski_triangle_obj.__exit__()
