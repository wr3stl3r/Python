'''picks random number from list.
if it's not in X, adds it to X list,
if X list does not have secret number,
random number is remuved from starting list
whit MAXGUES numbers
'''
import random
import time
MAXGUES = 100000 #bigger number longer it takes! or memo Error
UI = input("Enter number 0-{} so PC can guess it: ".format(MAXGUES))
pc_guess = [] # 0-MAXGUES
for i in range(0,MAXGUES+1):
	pc_guess.append(i)
#print(pc_guess) #CAUTION!!

pc_g_count = 1
X = []
while True:

	one = random.choice(pc_guess)
	#print(one)
	#print(UI, "<<")
	if str(one) not in X:
		X.append(str(one))
	
	if UI in X:
		print(".....Human look i did it. Numb is:", UI, "Human it took me:", pc_g_count, "guesses.")
		break
		
	pc_guess.remove(one)
	#print(X)
	pc_g_count +=1
	#time.sleep(0.5)
	if len(pc_guess) == MAXGUES-1:
		print("'-1' it ON?")
	if len(pc_guess) == round(MAXGUES*0.99):
		print("99 %")
	if len(pc_guess) == round(MAXGUES*0.98):
		print("98 %")
	if len(pc_guess) == round(MAXGUES*0.95):
		print("95 %")
		
	if len(pc_guess) == round(MAXGUES*0.9):
		print("90 %")
	if len(pc_guess) == round(MAXGUES*0.8):
		print("80 %")
	if len(pc_guess) == round(MAXGUES*0.7):
		print("70 %")
	if len(pc_guess) == round(MAXGUES*0.6):
		print("60 %")
	if len(pc_guess) == round(MAXGUES*0.5):
		print("50 %")
	if len(pc_guess) == round(MAXGUES*0.4):
		print("40 %")
	if len(pc_guess) == round(MAXGUES*0.3):
		print("30 %")
	if len(pc_guess) == round(MAXGUES*0.2):
		print("20 %")
	if len(pc_guess) == round(MAXGUES*0.1):
		print("10 %")
#print(X)

# (pc_guess[0] - pc_guess[-1]) /2 = middle ?
