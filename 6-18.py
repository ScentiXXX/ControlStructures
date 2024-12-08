x = int(input('enter x coordinate: '))
y = int(input('enter y coordinate: '))

if x == 0 and y == 0:
  print(f'Point P({x}, {y}) is in the center of the coordinate system')
elif x == 0:
  print(f'Point P({x}, {y}) is in the x-axis')
elif y == 0:
  print(f'Point P({x}, {y}) is in the y-axis')
elif x > 0 and y > 0:
  print(f'Point P({x}, {y}) is in the first quadrant of the coordinate system')
elif x > 0:
  print(f'Point P({x}, {y}) is in the fourth quadrant of the coordinate system')
elif y > 0:
  print(f'Point P({x}, {y}) is in the second quadrant of the coordinate system')
else:
  print(f'Point P({x}, {y}) is in the third quadrant of the coordinate system')
