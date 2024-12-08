decimal = int(input('Enter decimal number: '))
quotient = decimal
binary = ''


while quotient != 0:
  binary = str(quotient % 2) + binary
  quotient = int(quotient / 2)

print(f'{decimal}(10) = {binary}(2)')

