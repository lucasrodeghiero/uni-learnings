import turtle

# draw a square at the origin (0,0) point with sides length

def drawSquare(t,length): # 2 parameters, turtle and length of a side
    t.setheading(270)
    for count in range(4): # runs the code 4 times to draw a square
        t.forward(length)
        t.left(90)

def main(): # read a valiue as the length of the square
    length = int(input('Length of a side: '))
    t = turtle.Turtle()
    drawSquare(t,length) #calls the function
    turtle.done()

main()
