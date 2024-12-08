old_price = int(input('Enter product old price: '))
new_price = int(input('Enter product new price: '))

dicount = 1 - (new_price / old_price)

if new_price / old_price > 0.1:
  print('Buy the product!!')

print(f'Product price reduced by {round(dicount * 100)}%')
