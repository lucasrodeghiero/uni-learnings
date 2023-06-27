import turtle, random

# draw a square at the origin (0,0) point with sides length
def drawSquare(t, x, y, length):
    t.up() # lift up
    t.goto(x,y) # goes to the position
    t.down() # put it down to draw
    t.setheading(270)
    t.width(7)
    turtle.colormode(255)
    t.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    for count in range(4):
        t.forward(length)
        t.left(90)

def main():
    x = int(input('X value: '))
    y = int(input('Y value: '))
    length = int(input('Length of a side: '))
    t = turtle.Turtle()
    t.color('navy')
    t.begin_fill()
    drawSquare(t, x, y, length)
    t.end_fill()
    turtle.done()
main()
