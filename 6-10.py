###
# Calculating dog human age
#
years = int(input('Enter dog age in years: '))

if years <= 2:
  print(f'Dog age in human years is equal to: {years * 10.5}')
else:
  age = (years - 2) * 4 + 21
  print(f'Dog age in human years is equal to: {age}')
