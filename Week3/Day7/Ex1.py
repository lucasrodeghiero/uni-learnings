import turtle

unnamed = turtle.Turtle()
# Step 1
unnamed.setheading(90)
unnamed.forward(40)
# Step 2
unnamed.right(90)
unnamed.forward(40)
# Step 3
unnamed.left(90)
unnamed.forward(40)
# Step 4
unnamed.right(90)
unnamed.forward(80)
# Step 5
unnamed.right(90)
unnamed.forward(40)
# Step 6
unnamed.left(90)
unnamed.forward(40)
# Step 7
unnamed.right(90)
unnamed.forward(40)
#Step 8
unnamed.right(90)
unnamed.forward(160)
print(unnamed.position())
turtle.done()


  t = turtle.Turtle()
    t.width(4)
    t.speed(0)
    t.color('red')
    t.penup() # lift pen before moving to coordinate
    t.goto(x,y)
    t.pendown() # put it down at the new coordinate
    t.setheading(90)
    #t.forward(rad)
    t.setheading(180)
    #t.begin_fill() # commented out to stop filling the circle
    for count in range(120):
        t.left(3)
        t.forward((2 * math.pi * rad)/120)
    t.setheading(0)
    #t.forward(rad)
    #t.end_fill() # commented out to stop filling the circle
    t.hideturtle()
    turtle.done()

def main():
    rad = float(input('Radius: '))
    x = float(input('X: '))
    y = float(input('Y: '))
    drawCircle(x,y, rad)
