'''Binary search method
Creates a list of MAXGUES numbers,
asks Computer asks is your secret number
higher or lower that the middle number of list
when list is down to 2 or less numbers
Computer guesses number from them
''' #You can set that 2 to 3 or higher :)
import random
import time
import sys

MAXGUES = 10000000 #1&8zero=memoError
print(random.randint(0,MAXGUES), "Wana try your secret number to be REALY random?")
UI = input("Enter number 0-{} so PC can guess it: ".format(MAXGUES))
#pc_guess = [0,1,2,3,4,5,6,7,8,9,10]

pc_guess = [] # 0-MAXGUES
for i in range(0,MAXGUES+1):
	pc_guess.append(i)
#print(pc_guess) #CAUTION!!

pc_g_count = 1
X = []

def searcher():
	one = random.choice(pc_guess)
	#print(one)
	#print(UI, "<<")
	
	if str(one) not in X:
		X.append(str(one))
	
	if UI in X: #or UI == pc_guess[len(pc_guess)//2]:		
		print(".....Human look i did it. Numb is: '{}' Human it took me: {} guesses.".format(UI, pc_g_count))
		sys.exit()
		
	pc_guess.remove(one)
	#print(X, "<-- X")
	
def H_or_L():
	#FIRST = pc_guess[0]
	#LEN = len(pc_guess) #or the last number
	#mid = (len(pc_guess)//2)
	ask_2_human = input("Is your number higher or lower than {}? 'H' or 'L' :".format(pc_guess[len(pc_guess)//2]))
	if ask_2_human.upper() == 'L':
		del pc_guess[(len(pc_guess)//2):(len(pc_guess))] #del from Mid to Last
	if ask_2_human.upper() == 'H':
		del pc_guess[0:(len(pc_guess)//2)] #del from First to Mid
	
	#print(pc_guess, "<-- PC guess")
	
while True:
	#print(pc_guess[len(pc_guess)//2], "MID", UI, "user input") #remove #to see mid numb and input
	#you can test what happens if your secret number is (0-100)/2 or 50 or 25
	if UI == str(pc_guess[len(pc_guess)//2]): #Check if Mid == or != Secret number!
		print(".....Human look i did it. Numb is: '{}' Human it took me: {} guesses.".format(UI, pc_g_count))
		sys.exit()
	if len(pc_guess) > 2:
		H_or_L()
	
	if len(pc_guess) <= 2:
		searcher()
	#print(pc_g_count) #remove this!
	pc_g_count +=1

