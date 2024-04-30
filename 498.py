"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find gcd of two positive integers.
'''

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

'''
Standard answer: 
def gcd(x, y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd
'''
assert gcd(12, 17) == 1
assert gcd(4,6) == 2
assert gcd(2,9) == 1
