def circular_shift(lst1, lst2, n):
	#if abs(n) == len(lst1):
		#n *= -1
	while n < 0 -len(lst1):
		n += len(lst1) 
		
	if n < 0:
		n = n + len(lst1)
	#if len(lst1) % 2 == 1 and n != len(lst1): # and n +1 != len(lst1)
		#n += 1
		
	if n > len(lst1):
		n = n % len(lst1)

	NL = [lst1, lst2]
	TL = [] #test list
	for i in range(len(lst1)): #0,1,3...last
		if i+n >= len(lst1): #L=4 // i1--2=3
			i -= len(lst1)
		#print(i,'i')
		#print(n, 'n')
		TL.append(NL[1][i]==NL[0][i+n]) #i-n ??	
	
	return TL
# i=1+2     i=2+2      i=3+2 
#L11==L03 #L12==L01 #L13==L02
print(circular_shift([1, 2, 3, 4],[3, 4, 1, 2],2))# True) L1,i3 == L0,1 (i3--2=5)
print(circular_shift([1, 1],[1, 1],6))# True) len = 2 // 0-6 = -6
print(circular_shift([0, 1, 2, 3, 4, 5],[3, 4, 5, 2, 1, 0],3))# False)
print(circular_shift([0, 1, 2, 3],[1, 2, 3, 1],1), '1 even')# False)
print(circular_shift(list(range(32)),list(range(32)),0))# True)
print(circular_shift([1, 2, 3], [1, 2, 3],3), '3')# True)
print(circular_shift([5, 7, 2, 3],[2, 3, 5, 7],-2), '-2')# True) II[2]=5 // I[2--2=4]=I[0]=Error len=4

print(circular_shift([2, 3, 5, 7],[2, 3, 5, 7],-4), '-4')
print(circular_shift([2, 3, 5, 7,87],[2, 3, 5, 7,87],-4), '-4, and odd')
print(circular_shift([3,1,2],[1,2,3],-2), '-2, and odd')
print(circular_shift([3, 1, 2], [1, 2, 3],1), '1 odd') #True +1 if len lst1 odd
print(circular_shift([7, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7],1), '1 odd with 7') #True +1 if len lst1 odd len 7
print(circular_shift([2, 3, 1], [1, 2, 3],2), '2 odd') #True +1 if len lst1 odd
print(circular_shift([7, 2, 3, 5],[2, 3, 5, 7],-7), '-7') #
print(circular_shift([7, 2, 3, 5],[2, 3, 5, 7],-16), '-16') #
'''                            3      1
NL 1 i0 == 0 i0--2
NL 1 i1 == 0 i1--2 #=3 len(lst1)-1
NL 1 i2 == 0 i2--2 #=4 len(lst1)-1 i
NL 1 i3 == 0 i3--2
'''
