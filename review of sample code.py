# Author: <Zoe McClary>
# Creation Date: <5/10/2020>

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
#'while' line had 2 indentations, was fixed to have only 1. 'print' and 'cave' lines also has too many indentaions, was fixed to correct number
    while cave != '1' and cave != '2':
#added user input
        print(input('Which cave will you go into? (1 or 2)' ))
        cave = input
#'return' line had 2 indents, was fixed to only 1
#'caves not defined, fixed to 'cave'
        return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
#missing parenthesis on print line, added parenthesis. Also removed extra space
		print('Gobbles you down in one bite!')

playAgain = 'yes'
# added == inctead of '='
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
#'choosecave does not match, fixed to 'chooseCave'
	caveNumber = chooseCave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing")


