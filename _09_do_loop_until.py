anwser = '0'
#if you want to use the variable, you must initialization it before while
while anwser != '4':
    anwser = input("What is 2 + 2 ")
print("Yes! 2 + 2 = 4")

#while in turtle
import turtle
counter = 0
while counter < 4:
    turtle.forward(100)
    turtle.right(90)
    counter = counter + 1
# counter += 1 can be used but ++ cannot work