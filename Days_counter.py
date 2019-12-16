#!/usr/bin/env python
# coding: utf-8

def isLeapYear(year):
    """
    This function will Return True for a leap year
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def dayInMonth(year, month):
    """
    This function will return the number of days in a month
    """
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
        return 31
    else :
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30
        

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    """
    if day < dayInMonth(year,month):
        return year, month, day + 1
    elif month < 12:
        return year, month + 1, 1
    else:
        return year + 1, 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """
    This is a helper function for daysBetweenDates for calculating the stop of while loop
    """
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    
    assert dateIsBefore(year1, month1, day1, year2, month2, day2)

    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

#Test cases
daysBetweenDates(2019,10,10,2019,10,11)
daysBetweenDates(2019,10,10,2019,12,11)
daysBetweenDates(2019,10,10,2020,10,10)
daysBetweenDates(2018,10,10,2019,10,10)




