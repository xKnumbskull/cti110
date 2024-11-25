import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Initials - N and W")

# Create a turtle instance
t = turtle.Turtle()
t.color("red")
t.pensize(3)  # Set pen size to normal

# Draw the initial "N"
t.penup()
t.goto(-100, 0)  
t.pendown()
t.setheading(90)  
t.forward(100)    
t.right(135)
t.forward(140)    
t.left(135)
t.forward(100)    

# Start for the "W" 
t.penup()
t.goto(10, 100)     
t.pendown()
t.setheading(270)  

# Draw the initial "W"
t.forward(100)    
t.left(135)
t.forward(50)     
t.right(90)
t.forward(50)     
t.left(135)
t.forward(100)    

turtle.done()
