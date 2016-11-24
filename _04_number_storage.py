#if we dont put quote after relavant quotation, there will be number.
age = 42
high = 5
width = 30
area = high * width
print(area)
print(high**2) # high * high

#we cannot use + to combine number and a string

#print("the area of rectangle is" + area) this is wrong

#we can use %d to print numbers
#d is for decimal,f is for float
print("I have %d cats" % 6)     #I have 6 cats
print("I have %3d cats" % 6)    #I have   6 cats
print("I have %03d cats" % 6)   #I have 006 cats
print("I have %f cats" % 6)     #I have 6.000000 cats
print("I have %.2f cats" % 6)   #I have 6.00 cats

#you can also use a format method to format numeric values
print("I have {0:d} cats".format(6))     #I have 6 cats
print("I have {0:3d} cats".format(6))    #I have   6 cats
print("I have {0:03d} cats".format(6))   #I have 006 cats
print("I have {0:f} cats".format(6))    #I have 6.000000 cats
print("I have {0:2f} cats".format(6))    #I have 6.00 cats

#you can use a slack lash to indicate a command continues on the next line
print("The first area is {0:d} and".format(6) + "the second area is {0:f} and".format(50) \
    + " the third one is {0:2f}".format(area))
#dont delete that Tab before the second line. Not only it is about readiness but a normal format to code

