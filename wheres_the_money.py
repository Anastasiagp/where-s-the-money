###
### Author: Anastasia Pavlopoulos
### Description: An interactive program that calculates different aspects of one's money management
###
###

print('-----------------------------')
print("----- WHERE'S THE MONEY -----")
print('-----------------------------')
##code that the user enters in
annual_salary = input('What is your annual salary? \n')
numeric_1 = annual_salary.isnumeric()
if numeric_1== False or int(annual_salary) <0:
    print('Must enter positive integer for salary.')
    exit(0)

mortgage_rent = input('How much is your monthly mortgage or rent? \n')
numeric_2 = mortgage_rent.isnumeric()
if numeric_2== False or int(mortgage_rent)<0:
    print('Must enter positive integer for mortgage or rent.')
    exit(0)
mortgage_rent=float(mortgage_rent)
mp = (mortgage_rent)*12 / float(annual_salary)*100

bills = input('What do you spend on bills monthly? \n')
numeric_3 = bills.isnumeric()
if numeric_3== False or int(bills)<0:
    print('Must enter positive integer for bills.')
    exit(0)
bills=float(bills)
bp = (bills)*12 / float(annual_salary)*100


expenses = input('What are your weekly grocery/food expenses? \n')
numeric_4 = expenses.isnumeric()
if numeric_4==False or int(expenses)<0:
    print('Must enter positive integer for food.')
    exit(0)
expenses=float(expenses)


travel = input('How much do you spend on travel annually? \n')
numeric_5= travel.isnumeric()
if numeric_5==False or int(travel)<0:
    print('Must enter positive integer for travel.')
    exit(0)
travel=float(travel)
tp = (travel*100)/float(annual_salary)

annual_salary=int(annual_salary)
# taxes:
if annual_salary <= 15000:
    tax = 10
elif annual_salary <= 75000:
    tax = 20
elif annual_salary <= 200000:
    tax = 25
elif annual_salary >= 200000:
    tax = 30

# percent of annual salary
percent = annual_salary * (tax / 100)
if percent >= 50000:
    percent = 50000

extra = annual_salary - mortgage_rent - bills - expenses - travel

##code to determine how many pound symbols(hashtags) and dashes(-) are needed
hashtags = float(mortgage_rent)*12/float(annual_salary)*100
hashtags = int(hashtags)
hashtags_2=float(bills)*12/float(annual_salary)*100
hashtags_2=int(hashtags_2)
food_per= float(expenses)*52/(annual_salary)*100
hashtags_3=int(food_per)
hashtags_4=float(travel/annual_salary*100)
hashtags_4=int(hashtags_4)
hashtags_5=int(tax)
extra=annual_salary-(mortgage_rent*12+bills*12+expenses*52+travel+(tax/100)*(annual_salary))
extra_per=float(extra/annual_salary*100)
hashtags_6=int(extra_per)

dash_1=hashtags
dash_2=hashtags_2
dash_3=hashtags_3
dash_4=hashtags_4
dash_5=hashtags_5
dash_6=hashtags_6
dashes=max(dash_1,dash_2,dash_3,dash_4,dash_6)

##code that prints out the box that the answers will show up in
print('')
print('-'*45+dashes*'-')
print('See the financial breakdown below, based on a salary of $' + str(annual_salary))
print('-'*45+dashes*'-')
print('| mortgage/rent | $', format(mortgage_rent*12,'11,.2f'),'|',format( mp, '6,.1f'),'% |','#'*hashtags)
print('|         bills | $', format(bills*12,'11,.2f'),'|',format( bp, '6,.1f'),'% |','#'*hashtags_2)
print('|          food | $', format(expenses*52,'11,.2f'),'|',format( food_per,'6,.1f'),'% |','#'*hashtags_3)
print('|        travel | $', format(travel,'11,.2f'),'|',format( tp, '6,.1f'),'% |','#'*hashtags_4)
print('|           tax | $', format(percent,'11,.2f'),'|',format( tax, '6,.1f'),'% |','#'*hashtags_5)
print('|         extra | $', format(extra,'11,.2f'),'|',format( extra_per,'6,.1f'),'% |','#'*hashtags_6)
print('-'*45+dashes*'-')

if percent == 50000:
    print(">>> TAX LIMIT REACHED <<<")
if extra < 0:
    print('>>> WARNING: DEFICIT <<<')


