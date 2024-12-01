###
# Checks if the given day number of the month is correct
#
month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
day_ok = False

if month == 2:
    days = 28
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31
else:
    days = 30

if day >= 1 and day <= days:
    day_ok = True

message = f'Day {day} for the month {month}'

if day_ok:
    print(f'{message} is correct')
else:
    print(f'{message} is not correct')
