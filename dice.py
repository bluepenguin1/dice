#this program will randomly roll a pair of dice
#then it will add the values of the roll
#ask the user to guess a number
#compare the user's guess to the total value
#decide a winner
#inform user who winner is

from random import randint #importing code that will be used later to roll the dice
from time import sleep

budget = 100


def get_user_wager():
    print('Your wager is ' + str(user_wager))
    return user_wager
    
def get_user_guess(): #this asks the user to guess what the total die roll will be
    user_guess = int(input('Pick a number between 2-12: '))
    print('You choose: ' + str(user_guess))
    return user_guess

def roll_dice(user_wager, budget): #rolls dice and compares total to user input, if they are the same the user wins
    first_roll = randint(1,6)
    second_roll = randint(1,6)
    total = first_roll + second_roll
    sleep(1)
    user_guess = get_user_guess()
    sleep(2)
    print('House first roll ' + str(first_roll))
    sleep(1)
    print('House second roll ' + str(second_roll))
    sleep(1)
        
    if user_guess >= 12 and user_guess <2:
        print('Choose a correct number')
    
    if user_wager > budget or user_wager < 1:
        print('Insufficient wager')
    
    if user_guess == total:
        print('You win!')
        budget = user_wager * 12
        return user_wager
    else:
        print('You lose... womp womp')
        return -user_wager
    

user_input = input("Welcome to Nikitha's casino. Would you like to play?")

while budget <= 100 and user_input == 'Yes' or 'yes':
    user_wager = int(input('Make a wager: '))
    budget = budget + roll_dice(user_wager, budget)
    print('Your total now is ' + str(budget))
    user_choice = input('If you would like to quit the game, press Q. If you want to keep playing, press Enter.')
    if user_choice == 'Q':
        break
    if budget <= 0:
        break



    
    