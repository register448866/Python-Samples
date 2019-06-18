numbers = [-5, -3, -7, -2, -4]

total = 0
counter = 0
max = numbers[0]
min = numbers[0]

for x in numbers:
    total = total + x
    counter = counter + 1
    if(x > max):
        max = x
    if (x < min):
        min = x
    
avg = total/counter

# PRINT RESULTS
print()
print('Total     : ' + str(total))
print('Average   : ' + str(avg))
print('Minimum   : ' + str(min))
print('Maximum   : ' + str(max))
print()


