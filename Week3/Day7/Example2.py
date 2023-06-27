import turtle

lazy = turtle.Turtle()

# Pen up - no line
lazy.up()
# moves lazy to (50,60) location, no line since tail up
lazy.goto(50,60)
# Pen down - start drawing
lazy.down()
# Move to location (100,100)
lazy.goto(100,100)
# complete
turtle.done()
