rows = int(input("Inter number of rows: "))
STAR = "*"
SPACE = " "
count_spaces = rows - 1
count_stars = 1
COEFF = 2

for row in range(rows):
    print(SPACE * (count_spaces - row) + STAR * (count_stars + row * COEFF))
