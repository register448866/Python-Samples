
# Initialzing calculator
intro    = ' COMPOUND INTEREST CALCULATOR'
space    = '==============================================='
empty    = ''
p_prompt = ' Starting Principle Amount : $ '
i_prompt = ' Interest Rate             : % '
t_prompt = ' Time Invested For         :   '
c_prompt = ' Compound Per Time Unit    :   '
i_result = ' Total Compound Interest   : $ '
a_result = ' Final Amount              : $ '

# Capturing input 
print(empty)
print(space)
print(intro)
print(space)

principal = input(p_prompt)
interest_rate = input(i_prompt)
compounded = input(c_prompt)
time = input(t_prompt)

# Calculation
principal_float = float(principal)
interest_rate_float = float(interest_rate)
compound_float = float(compounded)
time_float = float(time)
final_amount = principal_float*((1+(interest_rate_float/(100*compound_float)))**(compound_float*time_float))

# Result
print(empty)
print(space)
print(i_result + str(round((final_amount - principal_float), 2)))
print(a_result + str(round(final_amount, 2)))
print(space)
print(empty)