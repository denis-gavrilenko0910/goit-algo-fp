import turtle
def draw_branch(branch_length, angle, level):
    if level == 0:
        return
    else:
        turtle.forward(branch_length)
        turtle.right(angle)
        draw_branch(branch_length * 0.7, angle, level - 1)
        turtle.left(angle * 2)
        draw_branch(branch_length * 0.7, angle, level - 1)
        turtle.right(angle)
        turtle.backward(branch_length)

def draw_pythagorean_tree(level):
    turtle.speed(9)  # Fastest drawing speed
    turtle.left(90)  # Start facing upwards
    turtle.up()
    turtle.backward(100)  # Move back to start position
    turtle.down()
    turtle.forward(100)  # Move to the starting point of the tree
    turtle.down()
    draw_branch(100, 30, level)  # Start drawing branches
    turtle.done()
if __name__ == "__main__":
    level = int(input("Enter the recursion level for the Pythagorean tree (e.g., 5): "))
    draw_pythagorean_tree(level)
# This code uses the turtle graphics library to draw a Pythagorean tree fractal.

