# Program that simulates the operation of an electronic thermometer.
#
age = int(input('Enter second number: '))

if age < 13:
    print("under 13")
elif age <= 19:
    print("15 PLN")
else:
    print("20 PLN")
