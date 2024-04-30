"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether the given number is even or not using bitwise operator.
'''

def is_Even(n):
    return n & 1 == 0

'''
Standard answer: 
def is_Even(n) : 
    if (n^1 == n+1) :
        return True; 
    else :
        return False; 
'''
assert is_Even(1) == False
assert is_Even(2) == True
assert is_Even(3) == False
