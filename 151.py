"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether the given number is co-prime or not.
'''

def is_coprime(x,y):
    if x == 1 or y == 1:
        return True
    for i in range(2,min(x,y)+1):
        if x % i == 0 and y % i == 0:
            return False
    return True

'''
Standard answer: 
def gcd(p,q):
    while q != 0:
        p, q = q,p%q
    return p
def is_coprime(x,y):
    return gcd(x,y) == 1
'''
assert is_coprime(17,13) == True
assert is_coprime(15,21) == False
assert is_coprime(25,45) == False
