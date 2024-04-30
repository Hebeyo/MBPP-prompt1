"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the nth octagonal number.
'''

def is_octagonal(n):
	return 3 * n * n - 2 * n

'''
Standard answer: 
def is_octagonal(n): 
	return 3 * n * n - 2 * n 
'''
assert is_octagonal(5) == 65
assert is_octagonal(10) == 280
assert is_octagonal(15) == 645
