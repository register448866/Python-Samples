
number = int(input('pick an INTEGER...  '))
bracket = [number]

if number == 0:
    print('ERROR!')
while number != 0: 
    for i in bracket:
        response = ""
        for f in range(i):
            response = '*' + response
        print(response)