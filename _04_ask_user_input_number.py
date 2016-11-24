'''
salary = input("please enter your salary")
bonus = input("please enter your bonus")
paycheckAmount = salary + bonus
print(paycheckAmount)

this code has a bug: salary and bonus are both string, + only to combine salarybonus
e.g. salary = 500; bonus = 75; paycheckAmount = 50075
'''

#this is OK
salary = input("please enter your salary ")
bonus = input("please enter your bonus ")
paycheckAmount = float(salary) + float(bonus)
print(paycheckAmount)

