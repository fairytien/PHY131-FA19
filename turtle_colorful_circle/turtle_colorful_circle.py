# Ask the user for a radius and then draw a colorful circle with that radius.
# Make the center of the circle at the current location of the turtle.

import sys
sys.setExecutionLimit(100000)
import turtle
wn = turtle.Screen()
tien = turtle.Turtle()
tien.pensize(5)

radius = int(input("Enter the radius for the circle:"))
pi = 3.14159265359
colors = ["purple","indigo","blue","teal","green","yellowgreen","gold","orange","pink","red","crimson","brown"]

tien.shape("circle")
tien.stamp()
tien.up()
tien.right(90)
tien.forward(radius)
tien.down()
tien.left(90)

for i in range(360):
    if i % 12 == 0:
        j = 0
    else:
        tien.color(colors[j])
        j += 1
    tien.forward(2*radius*pi/360)
    tien.left(1)