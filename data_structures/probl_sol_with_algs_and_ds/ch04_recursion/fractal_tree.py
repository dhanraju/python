"""Draw a Fractal tree.

The definition of fractal is that when you look at it the fractal has the same
basic shape no matter how much you magnify it. Some examples are the coastal
lines of continents, snowflakes, mountains and more.

Using this idea we could say that a tree is trunk, with a smaller tree going
off to the right and another smaller tree going off to the left. We will apply
the recursive definition of a tree to both of the smaller left and right trees.
"""
import turtle

class DrawFractalTree:
    def __init__(self):
        self.t = turtle.Turtle()
        self.my_win = turtle.Screen()
        self.t.left(90)
        self.t.up()
        self.t.backward(100)
        self.t.down()
        self.t.color("green")

    def draw_tree(self, branch_len):
        """Construct fractal tree."""
        # Make sure the branch_len is atleast greater than 5.
        if branch_len > 5:
            # Build right tree.
            self.t.forward(branch_len)
            self.t.right(20)
            # Recursively call by 20 degrees. Also subtract 15 from the
            # branch_len to make sure that the recursive trees get smallser and
            # smaller.
            self.draw_tree(branch_len - 15)
            # Build left tree
            self.t.left(40)
            # Recursively call by 40 degrees. The reason the turtle must turn
            # left by 40 degrees is that it needs to undo the original 20
            # degree turn to the right and then do an additional 20 degree turn
            # to the left in order to draw the left tree.
            self.draw_tree(branch_len - 10)
            self.t.right(20)
            self.t.backward(branch_len)

    def __exit__(self):
        """Exit windown on click."""
        self.my_win.exitonclick()


if __name__ == "__main__":
    draw_fractal_tree_obj = DrawFractalTree()
    draw_fractal_tree_obj.draw_tree(100)
    draw_fractal_tree_obj.__exit__()
