def is_prime(n):
    if n < 2:
        return False
    for i in range (2, n):        
        if (n%i) == 0:
            return False        
    return True
 		


def is_diabolic(n):
    text1 = str(n) 
    text2 = ("666")
    if (text2 in text1):
        return True
    else:
        return False

for i in range (100001):
    n = i
    if  is_diabolic(n) == True and is_prime(n) == True:
        print(f"{i}")
