'''Random e-mail generator!
Feel free to modify this py file ...
How you think how your random email should
look like :)'''

import os
import random
import names # https://github.com/treyhunner/names
# If you have troulbe installing names
# https://youtu.be/lvm6Q3SBJEk

'''TODO- make emails with random names from .txt file!!!!
I tryed to get random name from .txt file... i tryed all
Then i discovered random names :)

TODO2 - Understand what is the odds to write duplicate
emails in file...'''
#file usualy is saved where .py file is saved. But who knoes
print(os.getcwd(), '<... this is curent  working directory.\nFile will be saved here!')
print() #blank space
print("Sit back and chill. When Python is done\nemails will be printed on screen")
'''open a file'''
f = open("random_emails.txt", "a") #a-append(add to file) w-overwrite ALL!!!

'''Variables''' 
l_s = "BCDFGHJKLMNPRSTVZ" #consonants -Q -X (17)
p_s = "AEIOU" #Vowels -Y (5)
at = "@" # (1)
sign = ["_", "-", ".", ''] #(3) #'seperates' 'name' from birth year
domains = ["gmail.com", "yahoo.com", "hotmail.com", "hotmail.co.uk", "mail.ru", "mail.com"] #0-5 (6)

'''the email generatior'''
#devide by 3 because each loop makes 3 emails
for for_boss in range(20000//3 + 1): #prints number of emails in brackets
	'''Example''' # Randname-lapig-1999@gmail.com
	r_emails = (names.get_first_name()+sign[random.randint(0,2)]+random.choice(l_s) \
	+random.choice(p_s)+random.choice(l_s)+random.choice(p_s) \
	+random.choice(l_s)+sign[random.randint(0,3)] \
	+str(random.randint(1970,2005))+at+domains[random.randint(0,5)])
		
	'''Example''' # Randname.99@yahoo.com
	r_emails2 = (names.get_first_name()+sign[random.randint(0,3)] \
	+str(random.randint(70,99))+at+domains[random.randint(0,5)])
		
	'''Example''' # full_name@yahoo.com
	#get first name & last name. replace ' ' with random sing!
	r_emails3 = names.get_full_name().replace(' ', sign[random.randint(0,2)]) \
	+at+domains[random.randint(0,5)]
	f.write(r_emails.capitalize()) #Capitalize - First letter big rest small
	f.write("\n")
	f.write(r_emails2.capitalize())
	f.write("\n")
	f.write(r_emails3.capitalize())
	f.write("\n")

f.close()
#open and read the file after the appending or writing:
f = open("random_emails.txt", "r") #r is for reading olny!!!
print(f.read())





'''Posible combinations'''
#emails - 5494*3*(17*5*17*5*17)*4*(36)*6 = 1749083025600 ~ 1,7x10^12
#printing 10000//3 e-mails have 0,00032% chanse of getting duplicate

#emails2 - 5494*4*30*6 = 3955680 ~ 3,9x10^6
#printing 10000//3 e-mails have 75,44% chanse of getting duplicate

#emails3 - 5494*3*88000*6 = 8702496000 ~ 8,7x10^9
#printing 10000//3 e-mails have 0,06% chanse of getting duplicate

#https://github.com/treyhunner/names/blob/master/names/dist.male.first = 1219
#https://github.com/treyhunner/names/blob/master/names/dist.female.first = 4275
#https://raw.githubusercontent.com/treyhunner/names/master/names/dist.all.last =88k

'''These emails are like Birthday paradox'''
#https://betterexplained.com/articles/understanding-the-birthday-paradox/
#https://betterexplained.com/examples/birthday/birthday.html
#https://en.wikipedia.org/wiki/Birthday_problem

'''And that this why you need another .py file to check if there are duplicates
and another one to transver unique emails to new file'''

