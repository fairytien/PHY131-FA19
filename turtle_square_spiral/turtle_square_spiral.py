# Draw a spiral with squares of increasing length using turtle.

import sys
sys.setExecutionLimit(100000)
import turtle

tien = turtle.Turtle()
tien.color("crimson", "orange")

def turtle_square_spiral(my_turtle):
    wn = turtle.Screen()
    start_len = int(input("What's the starting length?"))
    num_spirals = int(input("How many spirals do you want?"))
    start_angle = 90

    for i in range(num_spirals):
        my_turtle.right(start_angle)
        my_turtle.forward(start_len)
        my_turtle.right(start_angle)
        my_turtle.forward(start_len)
        start_len += 7
        start_angle += 0.1
    return my_turtle

turtle_square_spiral(tien)