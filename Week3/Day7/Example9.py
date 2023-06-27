import turtle, random

#draws triangle at given coordinates x and y

def drawTriang(t, x, y, lenght):
    t.up() # lift up
    t.goto(x,y) # goes to the position
    t.down() # put it down to draw
    t.setheading(180)
    for i in range(3):
        t.forward(lenght)
        t.right(120)

def main():
    x = int(input('X value: '))
    y = int(input('Y value: '))
    length = int(input('Length of a side: '))
    t = turtle.Turtle()
    t.color('navy')
    t.begin_fill()
    drawTriang(t, x, y, length)
    t.end_fill()
    turtle.done()

main()
