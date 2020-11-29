def isPrime(X):
    C=0;
    n = 1;
    while n<X+1:
        if X % n ==0:         
            C+=1;
            n+=1;
        else:
            n+=1;
        if C>2:
            return False;
    return True;
    
print(isPrime(7));
