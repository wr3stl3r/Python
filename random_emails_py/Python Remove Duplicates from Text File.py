#Duplicate remover from!...
#https://www.youtube.com/watch?v=4hjtgn4_mJ4

from time import sleep
x = 4
while  x > 0:
	x = x -1
	print(x)
	sleep(0.7)
print("Python will remove duplicates and\nmake new file.")


'''File to remove from'''
#content = open('C:\\Users\\Kristaps\\Documents\\Files for Python\\randomnumbers.txt', 'r').readlines()
content = open('random_emails.txt', 'r').readlines()

content_set = set(content)

'''File to transver new and clean data!'''
cleandata = open('C:\\Users\\Kristaps\\Documents\\Files for Python\\random_emails_clean.txt', 'w')

for line in content_set:
	cleandata.write(line)

cleandata.close()
print()
print("..>>DONE<<..")
