#WEIGHT PROJECT:

weight = float(input('Weight: '))
measure = input('L(bs) or K(g): ')
measure1 = measure[0].upper()

if (measure1 == "K"):
    print(str('You are ' + str((weight / 0.454)) + ' pounds.'))
elif (measure1 == "L"):
    print(str('You are ' + str((weight * 0.454)) + ' kilograms.'))
else:
    print('Invalid!')

