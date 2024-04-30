"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the nth delannoy number.
'''

def dealnnoy_num(m, n):
    if m == 0 or n == 0:
        return 1
    return dealnnoy_num(m - 1, n) + dealnnoy_num(m - 1, n - 1) + dealnnoy_num(m, n - 1)

'''
Standard answer: 
def dealnnoy_num(n, m): 
	if (m == 0 or n == 0) : 
		return 1
	return dealnnoy_num(m - 1, n) + dealnnoy_num(m - 1, n - 1) + dealnnoy_num(m, n - 1)
'''
assert dealnnoy_num(3, 4) == 129
assert dealnnoy_num(3, 3) == 63
assert dealnnoy_num(4, 5) == 681
