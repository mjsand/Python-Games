from random import randrange

n = randrange(1000)

while True:
    g = int(input('Enter a number: '))
    
    if g == n :
        print('You Win!')
        break
    elif g < n :
        print ('Try a bigger number.')
    elif g > n :
        print('Try a smaller number.')
        