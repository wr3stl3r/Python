'''Let's try make this work with files'''
# https://thispointer.com/python-find-duplicates-in-a-list-with-frequency-count-index-positions/

# List of strings
#listOfElems = open('C:\\Users\\Kristaps\\Documents\\Files for Python\\randomnumbers.txt', 'r')
#listOfElems = open('random_emails.txt', 'r')
#listOfElems = open('C:\\Users\\Kristaps\\Documents\\Files for Python\\clean.txt', 'r')
listOfElems = open('C:\\Users\\Kristaps\\Documents\\Files for Python\\random_emails_clean.txt', 'r')

from time import sleep
x = 4
while  x > 0:
	x = x -1
	print(x)
	sleep(0.7)
print("Python will find duplicates in file. And show you if there are!")
print()

def getDuplicatesWithCount(listOfElems):
    ''' Get frequency count of duplicate elements in the given list '''
    dictOfElems = dict()
    # Iterate over each element in list
    for elem in listOfElems:
        # If element exists in dict then increment its value else add it in dict
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1    
 
    # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 i.e. only duplicate elements from list.
    dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
    # Returns a dict of duplicate elements and thier frequency count
    return dictOfElems

# Get a dictionary containing duplicate elements in list and their frequency count
dictOfElems = getDuplicatesWithCount(listOfElems)     
 
for key, value in dictOfElems.items():
        print(key.replace('\n', '') , ' - ', value) # '\n', '' #removes Enter after each line
