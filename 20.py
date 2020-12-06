# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
# Element Search
# Len is no good as index
# Cuz what do you do when search
# NR in other half of list!

def inside(List, user_input):
    if user_input in List:
        return True;
    else:
        return False;
        
def midIndx(X):
    res = int(len(X) // 2);
    return res;



def binarySearch(List,user_input):
    # 7 [1,2,3,4,5,6,7,8,9,10,11]
    list_even = True if len(List) % 2 == 0 else False;
    list_odd = True if len(List) % 2 == 1 else False;
    mid_inx = List[midIndx(List)];
    # List 
    while True:
        if user_input == mid_inx:
            return "YES you found it"
        elif user_input < mid_inx:
            List = List[?:midIndx(List)];
            mid_inx = List[midIndx(List)];
    
    
    
    
    
    
    
    





L = [i for i in range(1,52)];
UI = int(input("Hi! Is your number in list? Type here: "));
# ~ print(inside(L,UI));

print(len(L));
print(L);
print(f" mid Indx {midIndx(L)}");
print(binarySearch(L,UI));

