import math

def is_prime():    
    n =  int(input('Which number do you want to find if is Prime or not?'))
    if n <= 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    if n > 2 and n % 2 == 0:
        return False

    for i in range (2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    else :
        return True
    
result = is_prime()
if not result:
    print(f"It is not a prime!")
else:    
    print("It's a prime!")