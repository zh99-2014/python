#triple single quoto and double quote can be used for notes

#input function allows you to specific a message and returns the value typed in by users
#string in double quotes is hint showed to user
#'name' is variable to remember 'input'
name = input("What is your name?")
print(name)
anothername = "mary"
print(anothername)

#some rules:
#cannot contain any apsce
#any case sensitive: firstname and firstName will be two different variables
#cannot start with number
#and another tip: space is important in python, a space maybe change your code running way

#You can combine variables and strings with +
print("Hello " + name + " " + "and " + anothername)

#Demo1
animal = input("What is your favorite animal? ")
building = input("Name of a famous building: ")
color = input("What is yor favorite color? ")
print("Hickory Dickory Dock!")
print("The " + color + " " + animal + " ran up the " + building)

#Demo2
country = input("What country do you live in? ")
country = country.upper()   #All the letter will be changed into upper case
country = country.lower()   #All the letter will be changed into lower case
country = country.swapcase()#Change upper case letters into lower case, and lower case into upper case
#one of visual studio awesomeness is pop up list (Intellisense) followed by dot

#Demo3
message = "Hello world"
print(message.find('world'))        #print 6
print(message.count('o'))           #print 2
print(message.capitalize())         #print Hello world
print(message.replace('Hello','Hi'))#print Hi world

