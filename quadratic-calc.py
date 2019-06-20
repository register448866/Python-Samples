# Initialzing calculator
intro    = ' QUADRATIC EQUATION CALCULATOR'
space    = '==============================================='
empty    = ''
a_value = " 'a' value (coefficient of 'x^2' term) :  "
b_value = " 'b' value (coefficient of 'x^1' term) :  "
c_value = " 'c' value (coefficient of 'x^0' term) :  "

# Capturing input 
print(empty)
print(space)
print(intro)
print(space)

a_off = int(input(a_value))
b_off = int(input(b_value))
c_off = int(input(c_value))
equation = f"0 = {a_off}x^2 + {b_off}x + {c_off}"
print(equation)

# Calculation General
b_sq = b_off ** 2
minus_fourac = a_off * c_off * (-4)
inside_root = b_sq + minus_fourac
complete_root = inside_root ** 0.5
two_a = a_off * 2
neg_b = b_off * (-1)

# Calculation 1
numerator = neg_b + complete_root
answer = (numerator / two_a)

# Calculation 2
numerator_two = neg_b - complete_root
answer_two = (numerator_two / two_a)

# Result
print(empty)
print(space)
print("The first value of 'x' = " + str(answer))
print("The second value of 'x' = " + str(answer_two))
print(space)
print(empty)