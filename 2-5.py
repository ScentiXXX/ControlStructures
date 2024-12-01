###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

quarter = int((month - 1) / 3) + 1

print(f'Month {month} is in quarter {quarter}')
