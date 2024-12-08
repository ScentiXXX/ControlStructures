ean = input('Enter ean: ')

if len(ean) == 13:
  print('Article number is correct')
  if ean[:3] == '590':
    print('Article manufactured in Poland')
