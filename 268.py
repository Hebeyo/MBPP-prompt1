"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the n'th star number.
'''

def find_star_num(n):
    return 6 * n * (n - 1) + 1

'''
Standard answer: 
def find_star_num(n): 
	return (6 * n * (n - 1) + 1) 
'''
assert find_star_num(3) == 37
assert find_star_num(4) == 73
assert find_star_num(5) == 121
