import turtle

ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.color('light blue')
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30) #gap at the end of the line
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)


turtle.done()
