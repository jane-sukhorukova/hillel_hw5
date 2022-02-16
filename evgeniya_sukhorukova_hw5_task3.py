x = [12, 24, 66, 44, 76, 536]
counter = 0

while counter < len(x):
    if x[counter] % 2 == 0:
        counter += 1

    elif x[counter] % 2 != 0:
        print('NO')
        break
else:
    print('all numbers are even')
