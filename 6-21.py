amount = int(input('Enter the amount in PLN: '))
result = amount

coin_5 = int(result / 5)
result -= coin_5  * 5

coin_2 = int(result / 2)
result -= coin_2  * 2

coin_1 = int(result)
result -= coin_1

print(f'The amount of PLN 18 in coins: {amount}')
print(f'5 PLN coins: {coin_5}')
print(f'2 PLN coins: {coin_2}')
print(f'1 PLN coins: {coin_1}')

