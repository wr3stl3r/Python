from random import randint
print("Welcome to guessing game. Type 'exit' to stop game")
#https://www.w3schools.com/python/ref_func_round.asp
guessess = 0
victories = 0
while True:
	secret = randint(1,9)
	asknum = input("Enter a number from 1 to 9: ")
	
	if str(asknum) == 'exit':
		print("You have guessed ", guessess, "times. And you have won", victories, "times.")
		print( "Your win percentage is:", round(victories / guessess * 100, 1), "%")
		break
	
	if int(asknum) == secret:
		print(".......You have won. Num is: ", secret)
		victories += 1

	
	if secret > int(asknum):
		print("Number was higher! Try again!")
	else:
		print("Number was lower! Try again!")

	guessess += 1
