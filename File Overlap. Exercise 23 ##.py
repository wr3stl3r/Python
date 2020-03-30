'''Not the best solution, but it gets the job done!
it also adds \n to new list as '551\n'
but that does not bother python to find
overlaping numbers'''
prime = open('primenumbers.txt', 'r')
happy = open('happynumbers.txt', 'r')

#Adds primes to new list.
a = []
a.extend(prime)
b = []
b.extend(happy)
#Finds overlaping!
for i in a:
	if i in b:
		print(i.replace('\n', '')) #prints and removes Enter!

prime.close()
happy.close()
