'''
https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

print("Welcome to Fibonacci sequence!")
#add user input!
num1 = int(input("What the first number of sequence? :"))
num2 = int(input("What the second number of sequence? :"))
howmuch = int(input("How much numbers in sequence do you want?"))

X = []

d=0
for Fibo in range(howmuch-2):
	if len(X) == d: # 1*
		X.append(num1) # 2*
	d += 1
	if X[0]==num1 and len(X)<2: # 3*
		X.append(num2) # 4*
	
	if len(X) >= 2:		# 5*
		X.append(num1) # 6*
		X[-1] = X[-2]+X[-3] #*7

round_the_list = [round(num, 2) for num in X]
#round(num, digits) for num in X
print(round_the_list)
print("--------------------------------------------------")
print(".......The lenght of your list is:", len(X))
print("The sum of your list is:", sum(X))

if len(str(sum(X))) > 6:
	print("Deam!!!! Your sum is bigger than one million")

'''
1 - When there is 0 numbers in sequence.
2 - Python adds num1 in list X
X = [num1,]
3- When there is num1 in sequence and sequence is less that 2
4- Python adds num2 in list X
X = [num1, num2,]
5- When sequence is equal or larger than 2
6- Python adds num1 to list
X = [num1, num2, num1]
7- After num1 is added it changes num1 to sum of previus two
X[2](third) = becomes sum of previus two!
X = [num1, num2, (num1+num2)]

LOOP starts again!
1 & 2 - d = 1 and len(X) = 3 Python don't add num1
3 & 4 - first num = num1, but len(X) is 3 now
	So python dont add num2
5 & 6 & 7 - list or sequince is =2 or larger than to
Python will keep adding num1 to list and change it to sum of previus two!

After i finished this code i bearly understood it my self xD
U welcome!
'''







