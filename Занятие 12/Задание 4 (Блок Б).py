import math

def is_prime(n, divisor=None):
    if divisor is None:  
        divisor = 2

    if n <= 2:  
        return n == 2

    if divisor > math.isqrt(n): 
        return True if n > 1 else False  

    if n % divisor == 0:  
        return False

    return is_prime(n, divisor + 1)  

number = int(input("Введите натуральное число больше 1: "))
if is_prime(number):
    print("YES")
else:
    print("NO")

