#this program will randomly roll a pair of dice
#then it will add the values of the roll
#ask the user to guess a number
#compare the user's guess to the total value
#decide a winner
#inform user who winner is

from random import randint
from time import sleep

def get_user_guess():
    user_guess = int(input('Pick a number between 2-12: '))
    print('You choose: ' + str(user_guess))
    return user_guess

def roll_dice():
    first_roll = randint(1,6)
    second_roll = randint(1,6)
    total = first_roll + second_roll
    sleep(1)
    user_guess = get_user_guess()
    if user_guess == total:
        print('You win!')
    else:
        print('You lose... womp womp')
    
roll_dice()
    
    
    
    
    