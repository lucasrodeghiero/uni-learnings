import turtle

square = turtle.Turtle()

# drawing square

# turn
square.setheading(270)

# move and turn 4 times

for count in range (4):
    square.forward(140)
    square.left(90)


turtle.done()
