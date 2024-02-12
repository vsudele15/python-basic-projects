
#importing 'random' module
import random

#defining function to generate random number (1-6)
def roll():
    min_value=1
    max_value=6
    value=random.randint(min_value, max_value)

    return value

#taking valid input from the user
while True:
    players= input("Enter the number of players(2-4): ")
    #checking if the given input is a digit or not
    if players.isdigit():
        players= int(players)
        if 2<=players<=4:
            break
        else:
            print("Players should be between 2 and 4")
    
    else:
        print("Invalid Input! Try again")


max_score=50
#declaring a list to store the scores of each player
player_scores=[0 for _ in range(players)]


while max(player_scores)<max_score:
    #iterating over the list
    for player_idx in range(players):
        print("\nThe turn for player ", player_idx+1, "has just started!\n")
        print("Your total score so far is:", player_scores[player_idx] )
        #in every turn the current score starts from 0 and when the turn ends the current score gets stored at the specfic index for the player
        current_score=0

        while True:
            should_roll= input("Do you want to roll the dice (y)? ")
            if should_roll.lower()!="y":
                break
            value= roll()

            if value==1:
                print("You rolled a 1! Turn over!")
                #breaks out of the while loop if the rolled value is 1
                break
            else:
                print("You rolled a:", value)
                current_score+=value
            
            print("Your current score is:", current_score)
        
        #the score gets updated
        player_scores[player_idx]+= current_score
        print("Your total score is:", player_scores[player_idx])
    
#deciding the winner and printing it out
max_score= max(player_scores)
winning_index= player_scores.index(max_score)
print("Player ", winning_index+1, "is the winner with total score of", max_score)
        
