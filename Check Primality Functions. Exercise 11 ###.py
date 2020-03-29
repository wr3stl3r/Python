# Finding PRIME num = no divisors 3, 7, 11, 17, 4051

asknumb = input("Prime or NOT? >: ")
LOD = [] #list of divisors

print()
print("Your enered number is", str(len(asknumb)), "digits long.") 
print(".................................."*3)
print("Your", asknumb, "devisors are: \n")

#Find out users num's all divisors
i = 0
for i in range(int(asknumb)+1):
	i = i+1
	if int(asknumb) % i == 0:
		LOD.append(i)
print(LOD)


# Find out if user's number is Prime num.
print(".................................."*3)
Y = len(LOD)
if Y == 2: # all prime numbers have 2 divisors! (1 and itself)
	print("Congratulations you have found a PRIME!")
else:
	print("--NOT-- a Prime :(. Try different number! And maybe you will find a PRIME!")


#Thank u for using
print("\nDone!\nThank you for using our devisor and prime seeker!")
