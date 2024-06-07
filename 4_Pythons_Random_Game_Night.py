#Task 1: Random Choice Game
import random
items = ['chair', 'laptop', 'cup', 'keyboard', 'doughnut', 'monitor', 'speaker', 'mouse', 'desk'] #list of items to choose from

chosen_item = random.choice(items) #randomly choosing the answer

print(f"Items list: {items}") #printing the list of items for the play to choose from
play_again = True #establishing a variable to test for the loops conditions
while play_again: #loop to make the game repeatable
    player_choice = input("What item do you guess was chosen?: ") #gather the user's guess
    if player_choice == chosen_item: #Test if guess was correct
        print("You chose the right answer! Way to go!") #Winner message
    else:
        print("You did not choose the right item! Sorry.") #Loser message
    new_round = input("Try again? (y/n): ") # ask if they want to continue
    if new_round != 'y': #check if the user wanted to continue
        play_again = False #create a false condition to loop's conditional test
    else:
        continue #continue the loop if they did choose to go again