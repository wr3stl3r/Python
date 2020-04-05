'''
https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
Reverse Word Order
strings
'''
the_string = "a b c d e f g h i j k l m n o p r s t u v z"
words = "My name is Michele"
test_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

print("Original strings: ")
print(the_string)
print(words)
print("Original list: ")
print(test_list)

print("\nNow the strings and lists in reverse order!")
def reverse_string(enter):
	print(enter.split(' ')[::-1])
	
reverse_string(the_string)
reverse_string(words)

def reverse_list(thelist):
	d = 0
	f = -1
	COPY = thelist.copy()
	for i in range(len(thelist)):
		thelist[d] = COPY[f]
		d +=1
		f -=1
	print(thelist)

reverse_list(test_list)
