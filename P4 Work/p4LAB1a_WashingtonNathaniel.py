import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Square and Triangle")

# Create a turtle instance
t = turtle.Turtle()

# Draw a square using a for loop
t.color("blue")
for _ in range(4):
    t.forward(100)  # Adjust side length as needed
    t.right(90)

# Move the turtle to a new position for the triangle
t.penup()
t.goto(150, 0)  # Adjust position to avoid too much overlap
t.pendown()

# Draw a triangle using a for loop
t.color("green")
for _ in range(3):
    t.forward(100)  # Adjust side length as needed
    t.right(120)

# Finish
turtle.done()
