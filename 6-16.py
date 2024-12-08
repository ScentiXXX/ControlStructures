washing_product = input('Enter washing product: ')
rinse = input('Rinse (Y/N) ') == 'Y'
spin = input('Additional spin (Y/N) ') == 'Y'

time = 0

if washing_product == 'jacket':
  time += 40
elif washing_product == 'underwear':
  time += 70
elif washing_product == 'shoes':
  time += 20

if rinse:
  time += 15

if spin:
  time += 9

print(f'Total washing time: {time} minutes')
