import datetime

#we enter as birthday a string
#so we should convert a string to date with strptime() function

birthday = input("What is your birthday? (mm/dd/yyyy) ")
birthdate = datetime.datetime.strptime(birthday,"%m/%d/%Y").date()
#why did we list datatime twice?
#because we are calling the strptime function
#which is part of the datetime class
#which is in the datetime module
print ("Your birth month is " + birthdate.strftime('%B'))