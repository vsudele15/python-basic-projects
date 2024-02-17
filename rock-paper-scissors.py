import random

user_wins=0
computer_wins=0

options=["rock", "paper" ,"scissors"]
while True:
    user_input= input("Choose Rock/Paper/Scissors, Type Q to quit: ").lower()
    if user_input=="q":
        break
    
    if user_input not in options:
        print("Enter a valid input from Rock/Paper/Scissors")
        continue
    
    random_number= random.randint(0,2)
    computer_pick= options[random_number]
    print("The computer picked", computer_pick)

    if user_input=="rock" and computer_pick=="scissors":
        print("You won!")
        user_wins+=1
    elif user_input==computer_pick:
        print("You both picked the same. No wins")
        continue
        
    elif user_input=="paper" and computer_pick=="rock":
        print("You won!")
        user_wins+=1
    elif user_input=="scissors" and computer_pick=="paper":
        print("You won!")
        user_wins+=1
    else:
        print("You Lost..")
        computer_wins += 1

print("You won ", user_wins , "times.")
print("Computer won ", computer_wins , "times.")
print("Goodbye!")  
