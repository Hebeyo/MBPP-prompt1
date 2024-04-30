"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the nth decagonal number.
'''

def is_num_decagonal(n):
    return 4 * n * n - 3 * n

'''
Standard answer: 
def is_num_decagonal(n): 
	return 4 * n * n - 3 * n 
'''
assert is_num_decagonal(3) == 27
assert is_num_decagonal(7) == 175
assert is_num_decagonal(10) == 370
