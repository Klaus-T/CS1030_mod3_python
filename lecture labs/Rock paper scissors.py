from random import randint

player = input('rock (r), paper (p) or scissors (s)?')
#this is the categories for rock, paper, and scissor
print(player, 'vs ', end='')
#this whill display the players rock 'vs' the computers choice
chosen = randint(1,3)
#print(chosen)
#what this has done is it makes the computer choose a random number from 1-3, and below we designate what that number would mean
if(chosen == 1):
    computer = 'r'
#this is telling the computer that the random number 1 is a rock
elif(chosen == 2):
    computer = 'p'
#this is telling the computer that the random number 2 is paper
else:
    computer = 's'
#this is telling the comuter that because the others have been defined, that 3 will default as scissors
print(computer)

if(player == computer):
    print('Draw!')
#if the player and the computer chose the same thing its a draw
#below are all the other conditions of if the player has chosen if it beats the computers choice
elif(player == 'r' and computer == 's'):
    print('Player wins!')

elif(player == 'r' and computer == 'p'):
    print('Computer wins!')

elif(player == 'p' and computer == 'r'):
    print('Player wins!')

elif(player == 'p' and computer == 's'):
    print('Computer wins!')

elif(player =='s' and computer == 'p'):
    print('Player wins!')

elif(player == 's' and computer == 'r'):
    print('Computer wins!')
    