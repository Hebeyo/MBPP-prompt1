"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether the product of digits of a number at even and odd places is equal or not.
'''

def product_Equal(n): 
    n = str(n)
    odd = 1
    even = 1
    for i in range(0, len(n)):
        if i % 2 == 0:
            odd *= int(n[i])
        else:
            even *= int(n[i])
    if odd == even:
        return True
    return False

'''
Standard answer: 
def product_Equal(n): 
    if n < 10: 
        return False
    prodOdd = 1; prodEven = 1
    while n > 0: 
        digit = n % 10
        prodOdd *= digit 
        n = n//10
        if n == 0: 
            break; 
        digit = n % 10
        prodEven *= digit 
        n = n//10
    if prodOdd == prodEven: 
        return True
    return False
'''
assert product_Equal(2841) == True
assert product_Equal(1234) == False
assert product_Equal(1212) == False
