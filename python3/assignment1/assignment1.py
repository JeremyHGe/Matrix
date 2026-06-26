#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
Author: "Jeremy Hernandez"
Semester: "Fall/Winter/Summer 2026"

The python code in this file (assignment1.py) is original work written by
"Jeremy Hernandez". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys # Imports th system module, so that we are capable of using the functions within it

def day_of_week(year: int, month: int, date: int) -> str: # Expects values year, month, and date to be int, and the return value to be str
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] # List to conver number to day of the week
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4} # Tomohiko Sakamoto method of using the modulus of 7 on every month allowing to know the shift per month
    if month < 3: # Does not take into consideration January and February to avoid adding two leap days
        year -= 1 # To not affect the formula below it removes one year, so that the leap year is not counted
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7 # Calculates the shift of days in all of these according to the modulus of 7 on each
    return days[num] # Returns the day of the week due to the shift calculated as per the every 4, 100, and 400 years rules for leap years, offset of the month and day number


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    if leap_year(year) == True: # If leap year is true set feb_max as 29
        feb_max = 29 # Sets feb_max as 29
    else: # If leap year is false sets feb_max as 28
        feb_max = 28 # Sets feb_max as 28
    mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31} # Stores the max number of days per month
    return mon_max[month] # Returns the max number of days in the month

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This function has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-') # Splits the string according to -
    year = int(str_year)   # Converts to integer the str_year and saves as year
    month = int(str_month) # Converts to integer the str_month and saves as month
    day = int(str_day)     # Converts to integer the str_day and saves as day

    tmp_day = day + 1  # next day
    mon_maximum = mon_max(month, year) # Saves the max month number according to the month and year given
    if tmp_day > mon_maximum:           # Checks to see if the next day is above the month's maximum; follows through if true
        to_day = tmp_day % mon_maximum  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1              # Moves to next month as it cannot be above the month's maximum
    else:      # If the other statement false, follows
        to_day = tmp_day # Establishes the next day as a valid one
        tmp_month = month + 0 # Creates the tmp_month variable by copying the month by user, since there is no change in the month value

    if tmp_month > 12:  # If the next month is above the set amount of valid months it corrects to the next year
        to_month = 1    # Starts in 1st month
        year = year + 1 # Moves to next year
    else: # If the other statement false, follows
        to_month = tmp_month + 0 # No change in to_month

    next_date = f"{year}-{to_month:02}-{to_day:02}" # Prints the output after the checks that were done

    return next_date # Returns the next following date according to the date given


def usage(date):
    "Print a usage message to the user"
    if len(sys.argv) != 3:
        return "Please enter only 2 dates"
    if len(date) != 10:
        return "Please enter 10 characters for your date"
    if date[4] != '-' or date[7] != '-':
        return "Please separate your date using -"
    for c in date:
        if c not in ('1','2','3','4','5','6','7','8','9','0','-'):
            return "Please use numbers and - for formatting your date"
    
    str_year, str_month, str_day = date.split('-') # Splits the string according to -
    year = int(str_year)   # Converts to integer the str_year and saves as year
    month = int(str_month) # Converts to integer the str_month and saves as month
    day = int(str_day)     # Converts to integer the str_day and saves as day
    if month > 12 or month == 0:
        return "Please enter a valid month"
    if day > mon_max(month, year) or day == 0:
        return "Please enter a valid day"
    return True


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"

    lyear = year % 4 # Checks if the current year is a leap year by the remainder if 0 it is  aleap year
    if lyear == 0:   # Checks for the modulus if true it is a leap year if not it is not a leap year
        feb_max = 29 # this is a leap year
    else: # Checks for the modulus if true it is a leap year if not it is not a leap year
        feb_max = 28 # this is not a leap year

    lyear = year % 100 # Exception rule where every multiple of 100 year a year will not be a leap year even though it is a multiple of 4
    if lyear == 0:     # Checks for the modulus if true it is not a leap year 
        feb_max = 28   # this is not a leap year

    lyear = year % 400 # Exception to the exception where if it is a multiple of 400 it is a leap year
    if lyear == 0:     # Checks for the modulus if true it is a leap year 
        feb_max = 29   # this is a leap year

    if feb_max == 29:  # If feb_max equals 29 it means that this month is a leap year
        return True    # Hence leap year is true
    return False       # Hence leap year is false
def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    if len(sys.argv) != 3:
        return "Please enter only 2 dates"


    if len(date) != 10:
        return False
    if date[4] != '-' or date[7] != '-':
        return False
    for c in date:
        if c not in ('1','2','3','4','5','6','7','8','9','0','-'):
            return False
    
    str_year, str_month, str_day = date.split('-') # Splits the string according to -
    year = int(str_year)   # Converts to integer the str_year and saves as year
    month = int(str_month) # Converts to integer the str_month and saves as month
    day = int(str_day)     # Converts to integer the str_day and saves as day
    if month > 12 or month == 0:
        return False
    if day > mon_max(month, year) or day == 0:
        return False
    return True
def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    usage(start_date)
    usage(stop_date)
    if not valid_date(start_date):
        return usage(start_date)
    elif not valid_date(stop_date):
        return usage(stop_date)
    start_date, stop_date = earlier_date(start_date,stop_date)
    next_date = start_date # Placeholder for next_date
    weekends_total = 0     # Placeholder for total weekends
    while next_date != after(stop_date): # Runs until the stop date, but we check one day ahead to take into consideration the final day
        str_year, str_month, str_day = next_date.split('-') # Splits the string according to -
        year = int(str_year)   # Converts to integer the str_year and saves as year
        month = int(str_month) # Converts to integer the str_month and saves as month
        day = int(str_day)     # Converts to integer the str_month and saves as month
        current_day = day_of_week(year, month, day)
        if current_day in ('sat', 'sun'):
            weekends_total += 1
        next_date = after(next_date)
    return weekends_total

def earlier_date(start_date: str,stop_date: str):
    while True:
        """
        if not valid_date(start_date):
            print(usage(start_date))
            start_date = input("Enter start date (YYYY-MM-DD): ")
            stop_date = input("Enter end date (YYYY-MM-DD): ")
            continue

        if not valid_date(stop_date):
            print(usage(stop_date))
            start_date = input("Enter start date (YYYY-MM-DD): ")
            stop_date = input("Enter end date (YYYY-MM-DD): ")
            continue
"""
        str_start_year, str_start_month, str_start_day = start_date.split('-')
        start_year = int(str_start_year)
        start_month = int(str_start_month)
        start_day = int(str_start_day)

        str_stop_year, str_stop_month, str_stop_day = stop_date.split('-')
        stop_year = int(str_stop_year)
        stop_month = int(str_stop_month)
        stop_day = int(str_stop_day)

        if start_year > stop_year:
            print("Start date must be before end date.")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            stop_date = input("Enter end date (YYYY-MM-DD): ")
            continue
        elif start_year == stop_year and start_month > stop_month:
            print("Start date must be before end date.")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            stop_date = input("Enter end date (YYYY-MM-DD): ")
            continue
        elif start_year == stop_year and start_month == stop_month and start_day > stop_day:
            print("Start date must be before end date.")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            stop_date = input("Enter end date (YYYY-MM-DD): ")
            continue
        return start_date, stop_date

        

if __name__ == "__main__":
    print(usage(sys.argv[1],sys.argv[2]))
    day_count(sys.argv[1],sys.argv[2])