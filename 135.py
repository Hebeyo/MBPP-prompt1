"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the nth hexagonal number.
'''

def hexagonal_num(n): 
    return n*(2*n - 1)

'''
Standard answer: 
def hexagonal_num(n): 
	return n*(2*n - 1) 
'''
assert hexagonal_num(10) == 190
assert hexagonal_num(5) == 45
assert hexagonal_num(7) == 91
