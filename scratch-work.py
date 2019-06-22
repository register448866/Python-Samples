numbers = [32,11,15,28,22]
min = numbers[0]
for x in numbers:
    print('testing ' + str(x) + ' with ' + str(min))
    if(min > x):
        min = x

print("Minimum number is " + str(min))