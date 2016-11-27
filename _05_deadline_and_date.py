#import a library
import datetime

currentDate = datetime.date.today()
print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)
#python doesnt know what currentDate means until code is running
#thats why i didnt see IntelliSense
#python is a weekly method, i dont need to tell the type of a variable. I just through it a value
#so it has some sub-effect. I dont tell the type of currentDate, so pop up list dont know what should be contain

#and we can enter some code to display the date in different way
print(currentDate.strftime('%d %b,%Y'))
'''
%b is month abbreviation
%B is full month name
%y is two digit year
%a is the day of the week abbreviated
%A is the day of the week...
http://strftime.org/
http://babel.pocoo.org #some refencences
'''

