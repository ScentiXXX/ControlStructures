###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character), e.g.
# 'book' -> 'b o o k'
#
university = 'Krakow University of Economics'
university_expanded = university[0]

for char in university[1:]:
    university_expanded = university_expanded + " " + char

print(university) # original university name
print(university_expanded) # expanded university name