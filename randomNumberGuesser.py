
def randomNumberGame():
    from random import randrange
    
    n = randrange(100)
    count = 0
    while True:
        
        try: 
            guess = int(input('Enter a number: '))
            count += 1
        except ValueError:
            print('Error: Please enter an integer.')
            continue
        
        if guess == n :
            print('Congratulations! You won in', count, 'guesses.')
            replay = input('Would you like to play again? Yes or No: ').lower()
            if replay == 'yes' : randomNumberGame()
            else: break
            
                    
        elif guess < n :
            print ('Try a bigger number.')
        elif guess > n :
            print('Try a smaller number.')
            
randomNumberGame()