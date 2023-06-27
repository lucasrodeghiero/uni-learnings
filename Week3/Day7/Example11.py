import turtle, random
# draws a start at origin
def drawStar(t, length):
    t.speed(10)
    t.width(4)
    turtle.colormode(255)
    t.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    for i in range(5):
        t.forward(2 * length)
        t.right(144)

    t.width(7)
    turtle.colormode(255)
    t.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))

def main():
    length = int(input('Length of a side: '))
    t = turtle.Turtle()
    t.color('navy')
    t.begin_fill()
    drawStar(t, length)
    t.end_fill()
    turtle.done()
main()
