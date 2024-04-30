"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether the given number can be represented as difference of two squares or not.
'''

def dif_Square(n):
    for i in range(2, n):
        for j in range(2, n):
            if i*i - j*j == n:
                return True
    return False

'''
Standard answer: 
def dif_Square(n): 
    if (n % 4 != 2): 
        return True
    return False
'''
assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(15) == True
