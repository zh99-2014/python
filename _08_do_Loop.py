#an interesting turtle
import turtle
turtle.color('green')
turtle.forward(100)
turtle.right(45)
turtle.color('blue')
turtle.forward(50)
turtle.right(45)
turtle.color('pink')
turtle.forward(100)

#right(x)  left(x)  color('x')
#forward(x)  backward(x)

import turtle
#I want it loop four times
#and steps here is a variable
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
#only intented code is repeated
#and color is a proporty not a method/function, that's why we use quote

for steps in range(4):#an interesting picture
    turtle.forward(100)
    turtle.right(90)
    for moresteps in range(4):
        turtle.forward(200)
        turtle.right(90)

#also we can do like this
#it is an easy for us to draw a regular polygon
nbrsides = 6
for weidname in range(nbrsides):
    turtle.forward(100)
    turtle.right(360/nbrsides)
    for moresteps in range(nbrsides):
        turtle.forward(50)
        turtle.right(360/nbrsides)
