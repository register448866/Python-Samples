# THE SETS
set_one = [4, 5, 9, 2]
set_two = [-10, 0, 6, 7]
final = ""

# MULTIPLICATION RESULTS
for index in range(4):
    final = final + str(set_one[index] * set_two[index]) 
    if(index < 3):
        final = final + ', '

print('[' + final + ']')

final_one = (set_one[0] * set_two[0])
final_two = (set_one[1] * set_two[1])
final_three = (set_one[2] * set_two[2])
final_four = (set_one[3] * set_two[3])

# RESULTING SET
print()
print("RESULTING SET")
print("-------------")
print(f'[{final_one}, {final_two}, {final_three}, {final_four}]')