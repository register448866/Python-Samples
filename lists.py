# FIND LARGEST NUMBER IN A LIST

numbers = [5, 19.2, 1, -44, 3, 2, 4]

total = 0
largest_num = numbers[0]

for x in numbers:
    if(x > largest_num):
        largest_num = x

print()
print("LARGEST NUMBER IN THIS LIST IS:      " + str(largest_num))
print()