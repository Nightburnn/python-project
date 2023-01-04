#!/usr/bin/python3
#welcome User
print("Hello, Welcome to second's in a year")

#Ask user for days
days_this_year = int(input("\nHow many days are in this year?"))

#number of days in both leap year and none-leap year
days_in_year = 365
days_in_leapyear = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

# 365 * 24 * 60 * 60
result = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

# 366 * 24 * 60 * 60
leapyear_result = days_in_leapyear * hours_in_day * minutes_in_hour * seconds_in_minute

 # if its a leap year call on 366 * 24 * 60 * 60
if days_this_year == 366:
  print("Number of seconds in a leap year are", leapyear_result)
  # else 355 * 24 * 60 * 60(note user input won't matter still going to be getting answer for leap year or not)
else:
  print("Number of seconds in a year are", result)
