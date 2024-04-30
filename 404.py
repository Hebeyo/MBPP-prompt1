"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the minimum of two numbers.
'''

def minimum(a,b):
  return a if a<=b else b

'''
Standard answer: 
def minimum(a,b):   
    if a <= b: 
        return a 
    else: 
        return b 
'''
assert minimum(1,2) == 1
assert minimum(-5,-4) == -5
assert minimum(0,0) == 0
