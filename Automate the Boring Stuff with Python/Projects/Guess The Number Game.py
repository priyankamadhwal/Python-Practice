from random import randint
print('Hello player! Welcome to GUESS THE NUMBER game.')
name = ''
while name is '':
    name = input('Please enter your name : ')
print('Hey '+name+'! I am thinking of a number between 1 and 30.')
secretNumber, guess, chances = randint(1,30), 0, 10
while chances > 0:
    print('Take a guess? (You have '+str(chances)+' chances left.)')
    guess = int(input())
    if guess > secretNumber: print('Oops! Your guess is too high.')
    elif guess < secretNumber: print('Oops! Your guess is too low.')
    else: break
    chances -= 1
if guess == secretNumber: print('Good job, '+name+'!',"You've guessed the right number in "+str(10-chances+1)+' tries.')
else: print('Sorry '+name+', you failed. \nThe number i was thinking of was '+str(secretNumber)+'.')
