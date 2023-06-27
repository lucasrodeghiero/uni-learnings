import turtle, math
# House (1)
def drawHouse(house,length,x,y):
    house.speed('fast')
    house.penup()
    house.goto(x,y)
    house.pendown()
    house.seth(270)
    house.begin_fill()
    for count in range(4): # runs the code 4 times to draw a square
        house.fd(length)
        house.left(90)
    house.color('light yellow')
    house.end_fill()
    house.color('black')
    house.goto(x,y)
    house.seth(0)
    house.begin_fill()
    for i in range(3):
        house.fd(length)
        house.left(120)
    house.color('brown')
    house.end_fill()

# Boat (2)
def drawBoat(boat,length,x,y):
    boat.speed('fast')
    # Trapezium
    boat.penup()
    boat.goto(x,y)
    boat.pendown()
    boat.seth(0)
    boat.fd(1.8*length)
    boat.right(120)
    boat.fd(0.8*length)
    boat.seth(180)
    boat.fd(1*length)
    boat.seth(120)
    boat.fd(0.8*length)
    # Line
    boat.penup()
    boat.goto(x+0.9*length,y)
    boat.pendown()
    boat.seth(90)
    boat.fd(1.8*length)
    # Triangle
    boat.penup()
    boat.goto(x,y+0.25*length)
    boat.pendown()
    boat.seth(0)
    for i in range(3):
        boat.fd(1.8*length)
        boat.left(120)

# Car (3)
def drawCar(car,length,x,y):
    car.penup()
    car.goto(x,y)
    car.pendown()
    car.speed('fastest')
    car.seth(90)
    car.fd(0.4*length)
    car.right(90)
    car.fd(0.4*length)
    car.left(90)
    car.fd(0.4*length)
    car.right(90)
    car.fd(0.8*length)
    car.right(90)
    car.fd(0.4*length)
    car.left(90)
    car.fd(0.4*length)
    car.right(90)
    car.fd(0.4*length)
    car.right(90)
    car.fd(1.6*length)
    car.penup() # lift pen before moving to coordinate
    car.goto(x+0.4*length,y)
    car.pendown() # put it down at the new coordinate
    car.seth(90)
    car.seth(180)
    for count in range(120):
        car.left(3)
        car.fd((2 * math.pi * 0.2 * length)/120)
    car.seth(0)
    car.penup() # lift pen before moving to coordinate
    car.goto(x+1.2*length,y)
    car.pendown() # put it down at the new coordinate
    car.seth(90)
    car.seth(180)
    for count in range(120):
        car.left(3)
        car.fd((2 * math.pi * 0.2 * length)/120)

def main():
    x = float(input("Enter the x coordinate: "))
    y = float(input("Enter the y coordinate: "))
    length = int(input('Enter the length of the shape: '))
    print(f"-----------Turtle Drawing Program-----------")
    print(f"Draw House (1), Draw Boat (2), Draw Car (3)")
    selection = int(input("Enter your selection: "))
    if selection == 1:
        house = turtle.Turtle()
        drawHouse(house,length,x,y)
        print(house.position())
        turtle.done()
    if selection == 2:
        boat = turtle.Turtle()
        drawBoat(boat,length,x,y)
        print(boat.position())
        turtle.done()
    if selection == 3:
        car = turtle.Turtle()
        drawCar(car,length,x,y)
        print(car.position())
        turtle.done()

main()
