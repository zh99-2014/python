import datetime

nextBirthday = datetime.datetime.strptime('12/20/2016','%m/%d/%Y').date()
currentDate = datetime.date.today()
#if you substract two dates you get back the number of days between those dates
diffenerce = nextBirthday - currentDate
print(diffenerce.days)