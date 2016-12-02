#steps at first is 0
for steps in range(4):
    print(steps)

#steps will be 1,2,3
for steps in range(1,4):
    print(steps)
#when steps equals range,it will stop. So it wont be 4

#steps will be 1,3,5,7,9
for steps in range(1,10,2):
    print(steps)
#the third word is a step for skip

#and you can exactly tell it what values your want to use in loop
for steps in [1,2,3,4,5]:
    print(steps)

#and you can even dont have to use numbers 
import turtle
for steps in ['red','green','blue','black']:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(90)

#and you can mix the numbers and strings
for steps in ['red','green','blue','black',8]:
    print(steps)
#and turtle cannot of course know what color 8 is,so dont use it in turtle.color()