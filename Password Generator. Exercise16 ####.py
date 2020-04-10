# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
#Write a password generator in Python. Be creative with how you generate passwords

import random
import string
import names #https://github.com/treyhunner/names

letters = string.ascii_letters
digits = string.digits
special = "~!@#$%^&*()`[]=+|?-_" # or string.punctuation

print('''Hello! Welcome to PW generator!
You can pick one of tree posible passwords!
weak   - Joann (1) or BrandyJoann (2)....
strong - Joann_3456 (1)or Joann_34563456 (2)...
insane - c7^vrQ-[q#tR]1 (14)....''')
print()
def gamestart():
	while True:
		wich_one = input("What kind of password do you want? (weak, strong or insane?): ")
		if wich_one.lower() == 'weak':
			weak()
		if wich_one.lower() == "insane":
			insane()
		if wich_one.lower() == "strong":
			strong()
		if wich_one.lower() == "quit":
			break
		if 'dirtyword' in wich_one.lower():
			print("Ohh you dirty! You eat bread whit those fingers?")
			break

def weak():
	howlong = input("How long you want your WEAK password (gives random names!): ")
	X = []
	for i in range(int(howlong)):
		X.append(names.get_first_name())		
	print(''.join(X))

def strong():
	howlong = input("How long you want your STRONG password: ")
	print(names.get_first_name()+'_'+(str(random.randint(1000,9999))*int(howlong)))

def insane():
	X = []
	howlong = input("How long you want your INSANE password: ")
	for i in range(int(howlong)):
		R = random.choice(letters+digits+special)
		X.append(R) 
	print(''.join(X), "<-- THIS IS YOUR PW")
	print(len(X), "<-- PW lenght")
	combinations = len(letters+digits+special)**len(X) #73**len(X)
	print(combinations, "<-- posible PW Combinations! It's {} digits!".format(len(str(combinations))))

if __name__ == "__main__":
	gamestart()


