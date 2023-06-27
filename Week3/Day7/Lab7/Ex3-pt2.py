import turtle, math, random

def drawCircle(x, y, rad):
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

main()
