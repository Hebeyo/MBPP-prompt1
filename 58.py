"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether the given two integers have opposite sign or not.
'''

def opposite_Signs(x,y): 
    return ((x < 0) ^ (y < 0));

'''
Standard answer: 
def opposite_Signs(x,y): 
    return ((x ^ y) < 0); 
'''
assert opposite_Signs(1,-2) == True
assert opposite_Signs(3,2) == False
assert opposite_Signs(-10,-10) == False
