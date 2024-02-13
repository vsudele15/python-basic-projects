import random

user_input= input("Enter a number: ")

if user_input.isdigit():
    user_input= int(user_input)

    if user_input<=0:
        print("Please enter a positive number next time")
        quit()

else:
    print("Please enter a digit next time")
    quit()

random_number= random.randint(0, user_input)
guesses=0
while True:
    guesses+=1
    user_guess= input("Enter a guess number: ")
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
        print("Please enter a digit next time")
        continue

    if user_guess==random_number:
        print("You got it!")
        break
    elif user_guess< random_number:
        print("Your guess is less than the actual number..Try again")
    else:
        print("Your guess is more than the actual number..Try again")

print("You got it in", guesses, "guesses")