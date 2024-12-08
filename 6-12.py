products_amount = int(input('Enter car speed: '))
products_price = int(input('Enter products price: '))

if products_amount >= 2:
  print(f'Amount to pay: {products_amount * products_price}')
else:
  product_final_price = (products_amount - 2) * (products_price * 0.75) + 2 * products_price
  print(f'Amount to pay: {product_final_price}')
