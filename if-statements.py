
credit = 333

if 800 <= credit:
    print("Down payment = $" + str(0.1 * 1000000))
elif 600 <= credit < 800:
    print("Down payment = $" + str(0.15 * 1000000))
else:
    print("Down payment = $" + str(0.2 * 1000000)) 
