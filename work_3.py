'''
3,4
****
****
****

'''

numbers = [5, 20]
for x in range(numbers[0]):
    answer = ""
    for y in range(numbers[1]):
        answer = "*" + answer
    print(answer)