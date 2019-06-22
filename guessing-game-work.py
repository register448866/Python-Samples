import random

print()
print('～～～～～～～～～～～～～～')
print('★ GUESS THE MAGIC NUMBER ★')
print('～～～～～～～～～～～～～～')
print()
print('''Instructions: The computer has        
randomly generated a magic number between     
1 and 50 and it is your job to guess what      
that number is! Every time you guess a number,  
the computer will tell you if your guess is     
too high or too low. You will keep guessing     
until you correctly guess the magic number.     
Try to guess the magic number in as few         
guesses as you can. Good luck!''')              
print()
print('～～～～～～～～～～～～～～')
print()

flag = True
while flag:
    #################################
    # GAME STARTS HERE
    #################################
    magic_number = random.randint(1, 50)
    guess = int(input('Please guess a number between 1 and 50! ⋙   '))
    counter = 0

    while guess != magic_number:
        counter = 1 + counter
        if 0 < guess < magic_number:
            print()
            print("Your guess is too low! Keep trying!")
            print()
            guess = int(input('Please guess again! ⋙   '))
        elif 50 > guess > magic_number:
            print()
            print("Your guess is too high! Keep trying!")
            print()
            guess = int(input('Please guess again! ⋙   '))
        elif guess > 50:
            print()
            print("The magic number cannot be more than 50!   ")
            print()
            guess = int(input('Please guess again! ⋙   '))
        elif guess < 1:
            print()
            print("The magic number cannot be less than 1!   ")
            print()
            guess = int(input('Please guess again! ⋙   '))
        else:
            print()
            print("Invalid input!")
            print()
            guess = int(input('Please guess again! ⋙   '))
    if guess == magic_number:
        print()
        print('～～～～～～～～～～～～～～')
        print("CONGRATS, YOU HAVE CORRECTLY GUESSED THE MAGIC NUMBER!")
        print(f"Number of attempts: {counter + 1}")
        print('～～～～～～～～～～～～～～')
        print()

    #################################
    # GAME ENDS HERE
    #################################
    x = input("Would you like to play again (y or n)? ")
    if x[0].lower() == "n":
        print('Have a good day')
        print()
        break