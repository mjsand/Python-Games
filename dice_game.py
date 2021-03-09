### the purpose of this file is to simulate a dice rolling game

import random
from random import randint

def diceRoll():

    x = randint(1, 6)
    guess = int(input('Enter your guess: '))
    
    print('You guessed', guess,'...', 'And the dice is...', x)
    
    if guess == x:
        print('Congrats! You win!')
    
    else:
        print('Sorry, you lost.')

diceRoll()