"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to left rotate the bits of a given number.
'''

def left_Rotate(n,d):
    return (n << d) | (n >> (32 - d))

'''
Standard answer: 
INT_BITS = 32
def left_Rotate(n,d):   
    return (n << d)|(n >> (INT_BITS - d))  
'''
assert left_Rotate(16,2) == 64
assert left_Rotate(10,2) == 40
assert left_Rotate(99,3) == 792
