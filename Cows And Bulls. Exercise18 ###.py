'''
https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
Cows And Bulls   
Exercise 18
gues 4 digit number!
...check link for more details!
'''

import sys
import random
import string

print("Welcome to the Cows and Bulls Game!")
print("For every number in the wrong place, you get a bull. For every one in the right place, you get a cow.")
print("The game ends when you get 4 cows!")
#corect place = COW
#wrong place = bull

def CandB():
	special = "[@_!#$%^&*()<>?/\|}{~:]`;+=-,./'¼"
	cheater = False
	guesses = 1
	XX = str(random.randint(1000, 9999)) # 4 dig numb can't be 22 so it start form 1k
	while True:
		#print(XX)
		player = input("Guess 4 digit number: ")
		COWS = 0
		BULL = 0
		if player.lower() == 'q':
			sys.exit()
		#prevents player for checking COW with none digits 11**
		for i in player:
			if i in string.ascii_letters+string.whitespace+special:
				cheater = True
		if cheater == True:
			print("GAME OVER!!")
			print("Don't cheat use only digits!")
			print("The scary number was:", XX)
			gamestart()
		#checks for cows (corect digit in corect place)
		if player[0]==XX[0]:
			COWS +=1
		if player[1]==XX[1]:
			COWS +=1
		if player[2]==XX[2]:
			COWS +=1
		if player[3]==XX[3]:
			COWS +=1
		#Finds a bull	
		if player[0] in XX and player[0] != XX[0]:
			BULL +=1
		if player[1] in XX and player[1] != XX[1]:
			BULL +=1
		if player[2] in XX and player[2] != XX[2]:
			BULL +=1
		if player[3] in XX and player[3] != XX[3]:
			BULL +=1
		#Checks if player have quessed the number
		if player == XX:
			print("You have WON")
			print("You guessed 4 digit number in ", guesses, "guesses.")
			gamestart()
		#Cheat! Python will print secret number :)
		if player == '000666000': 
			print(XX, "<<<Cheater! But i am not judging!")
		#prints how many cows and bulls after each guess
		print(COWS, "cows,", BULL, "bull")
		guesses += 1 #Adds one gues for every atempt

#Game start function
def gamestart():
	while True:
		ASK = input("Type 'go' to play cows and bulls or 'q' to exit: ")
		if ASK.lower() == 'go':
			CandB()
		if ASK.lower() == 'q':
			sys.exit()
		else:
			gamestart()

if __name__=="__main__":		
	gamestart()

