#answer = input("would you like express shipping? ")
#if answer.upper() == "yes":
#    print("that will be extra $10")
#    print("all right!")
#print("have a nice day!")

#colon and Tab indented is important
#without colon, it will show you errer
#without intented, it will be like:
#       if (answer == "yes");
#       print blablabla;
#intent means this sentence can only be done when if is yes
#other logical operators are the same with ones in other programing languages

#in order to make upper and lower cases consistant, we can code like that:
#   bestAnswer = "Yes"
#   if answer.upper() = bestAnswer.upper()
#       print blablabla

#deposit = input("What is your deposit? ")
#deposit = float(deposit)
#if deposit > 100:
#    print("You will get a free toaster")
#print("Have a nice day")

#deposit = input("What is your deposit? ")
#deposit = float(deposit)
#if deposit > 100:
#    print("You will get a free toaster")
#else:
#    print("Enjoy your mug!")
#print("Have a nice day")

#you can use a boolean variable to remenber if a condition is true or false
deposit = input("What is your deposit? ")
deposit = float(deposit)
if deposit > 100:
    freeToaster = True  #just like a flag
if freeToaster:
    print("Enjoy your toaster!")