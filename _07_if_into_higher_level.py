country = input("Where are you from? ").upper()
if country == "CANADA":
    print("Hello!")
elif country == "GERMANY":
    print("Guten Tag!")
elif country == "FRANCE":
    print("Bonjour!")
else:
    print ("OK")

#if it enter "if" and case is ture, print and then end the if
#and that why elif is not intented

#and can only be used for enter if when all variables are true
winLottery = True
bigWin = False
if winLottery and bigWin:
    print("You can retire.")
# and/or/not is three compareable operators
#of course,like in C/C++ programing,in fact i forgot,and/or, and will be evaluated first

country = input("your country: ").upper()
color = input("your color: ").upper()
fruit = input("your fruit: ").upper()
if country == "ENGLAND" and color == "RED" or fruit == "APPLE":
    print("YES")
#of course bracklet is a tool

monday = True
freshCoffee = False
if monday:
    #you would have cod here to check for fresh coffee
    #the if statement is nested, so this is statement
    #is only executed if the other if statement is true
    if not freshCoffee:
        print("go but a coffee")
    print("I hate Mondays")
print("Now you can start work")