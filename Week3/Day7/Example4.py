import turtle

unnamed = turtle.Turtle()
# initially lazy is at home pointing East.
print(unnamed.position())
print(unnamed.heading())

#move to 30, 40. Print and confirm
unnamed.goto(30,40)
print(unnamed.position())

#Home is (0,0) position in cartesian plane
unnamed.home()
print(unnamed.position())

# complete
turtle.done()
