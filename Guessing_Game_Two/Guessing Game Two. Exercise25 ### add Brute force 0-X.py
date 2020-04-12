'''
BRUTE FORCE method
from 0 till your number!
check one by one ...
its easy when UI=1 and insane when UI=maxgues
'''
import random
import time
MAXGUES = 10000000 #1&8zero=memoError
UI = input("Enter number 0-{} so PC can guess it: ".format(MAXGUES))
print("Finding number")
pc_g_count = 1
one = -1
while True:
	one += 1
	if UI == str(one):
		print("DONE!")
		print(".....Human look i did it. Numb is:", UI, "Human it took me:", pc_g_count, "guesses.")
		break

	pc_g_count +=1

	if one == round(MAXGUES*0.99):
		print("99 %")
	if one == round(MAXGUES*0.98):
		print("98 %")
	if one == round(MAXGUES*0.95):
		print("95 %")
		
	if one == round(MAXGUES*0.9):
		print("90 %")
	if one == round(MAXGUES*0.8):
		print("80 %")
	if one == round(MAXGUES*0.7):
		print("70 %")
	if one == round(MAXGUES*0.6):
		print("60 %")
	if one == round(MAXGUES*0.5):
		print("50 %")
	if one == round(MAXGUES*0.4):
		print("40 %")
	if one == round(MAXGUES*0.3):
		print("30 %")
	if one == round(MAXGUES*0.2):
		print("20 %")
	if one == round(MAXGUES*0.1):
		print("10 %")

