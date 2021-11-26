# import datetime
# birth_date = datetime.date(2000, 2, 1)
# end_date = datetime.date(2015, 3, 10)
# time_difference = end_date - birth_date
# age = time_difference.days
# print(age) 

# import datetime
# birth_date = datetime.date(BOD)
# end_date = datetime.date(current date)
# time_difference = end_date - birth_date
# age = time_difference.days
# print(age) 

# from datetime import date
# def calculateAge(birthDate):
#     today = date.today()
#     age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
#     return age
# print(calculateAge((age(1996,3,5),"years") 

import datetime
import pytz
    for tz in pytz.all_timezones:
        print tz
birth_year = int(input("enter the year of birth "))
birth_month = int(input("enter the month of birth "))
birth_day = int(input("enter the date of birth "))

current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day

age_year = (current_year - birth_year)
age_month = current_month - birth_month
age_day = current_day - birth_day

print(age_year,"years",age_month,"month",age_day,"day") 

