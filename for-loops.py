prices = [10, 20, 30]
total = 0

for xx in prices:
    total = xx + total
print("The avg. price for all items = $" + str(total/3))
    

for x in range(3):
    for y in range(3):
        print(f'({x}, {y})')