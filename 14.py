"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the volume of a triangular prism.
'''

def find_Volume(l,b,h):
    return (l*b*h)/2

'''
Standard answer: 
def find_Volume(l,b,h) : 
    return ((l * b * h) / 2) 
'''
assert find_Volume(10,8,6) == 240
assert find_Volume(3,2,2) == 6
assert find_Volume(1,2,1) == 1
