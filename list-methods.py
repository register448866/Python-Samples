numbers = [5, 4, 1, 2, 9, 9, 4, 4, 3]


listy = []

for number in numbers:
    if number not in listy:
        listy.append(number)

print(listy)