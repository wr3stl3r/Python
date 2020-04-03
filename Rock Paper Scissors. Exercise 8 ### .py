'''
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
Rock Paper Scissors   
Exercise 8 (and Solution)
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''
import getpass, os
#player1 = getpass.getpass('Rock, Paper, Scissors? ', stream = None)
#os.system('cls')
#Maybe should cut down Scissors to Sciss. So all inputs are ~equal by sound.
def gamelogic():
	Player1 = getpass.getpass("Player one please input weapon (Rock, Paper or Scissors): ")
	Player2 = input("Player TWO please input weapon (Rock, Paper or Scissors): ")

	if Player1 == Player2:
		print("Draw! Play again!P=", Player1, "P2=", Player2)

	if Player1 == 'Paper' and Player2 == 'Rock':
		print("Player one have WON! P=", Player1, "P2=", Player2)
	if Player1 == 'Rock' and Player2 == 'Scissors':
		print("Player one have WON! P=", Player1, "P2=", Player2)
	if Player1 == 'Scissors' and Player2 == 'Paper':
		print("Player one have WON! P=", Player1, "P2=", Player2)


	if Player1 == 'Paper' and Player2 == 'Scissors':
		print("Player >TWO< have WON! P=", Player1, "P2=", Player2)
	if Player1 == 'Rock' and Player2 == 'Paper':
		print("Player >TWO< have WON! P=", Player1, "P2=", Player2)
	if Player1 == 'Scissors' and Player2 == 'Rock':
		print("Player >TWO< have WON! P=", Player1, "P2=", Player2)
		
thegame = 'Start'
while thegame == 'Start':
	thegame = input("Enter: 'Start', to start or continue the game. or 'Quit' to quit: ")
	if thegame == "Start":
		gamelogic()
	if thegame != 'Start' and thegame !='Quit':
		print("START or QUIT! Are u stupid?")
	if thegame == "Quit":
		break
	
