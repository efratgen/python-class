#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:14:13 2022

@author: efrat
"""

import sys


def isPregnant(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            return False
        return True
    return False


def maxDaysMonth(m, y):
    # In case of February
    if m == 2:
        return 29 if isPregnant(y) else 28

    # In case of 30 days long month
    days30 = [4, 6, 9, 11]
    if m in days30:
        return 30

    # Default month are 31 days long
    return 31


def checkValidity(d, m, y, days_to_add):
    max_days = maxDaysMonth(m, y)

    # Days to add must be positive integer
    if days_to_add < 0:
        return False

    # Month must be between 1 to 12
    if m < 1 or m > 12:
        return False

    # A day in a month cannot exceed the maximal days in a certain month
    if d > max_days:
        return False

    return True


def future_date(day, month, year, days_to_add):
    # We go each day in the days to add
    for i in range(days_to_add):
        max_days = maxDaysMonth(month, year)
        if day == max_days: # In case of the last day in a month
            if month == 12: # In case of the last month in the year
                year += 1
                month = 1
            else:
                month += 1
            day = 0
        day += 1
    print(f'The future date will be: {day}/{month}/{year}')


def main():

    day = int(input("Day of birth: "))
    month = int(input("Month of birth: "))
    year = int(input("Year of bith: "))
    days_to_add = int(input("How many days to add: "))

    if checkValidity(day, month, year, days_to_add):
        future_date(day, month, year, days_to_add)
    else:
        print("error")
        sys.exit()


main()
