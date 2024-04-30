"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to calculate the nth pell number.
'''

def get_pell(n): 
    pell = [0] * (n + 1)
    pell[0] = 0
    pell[1] = 1
    for i in range(2, n + 1):
        pell[i] = 2 * pell[i - 1] + pell[i - 2]
    return pell[n]

'''
Standard answer: 
def get_pell(n): 
	if (n <= 2): 
		return n 
	a = 1
	b = 2
	for i in range(3, n+1): 
		c = 2 * b + a 
		a = b 
		b = c 
	return b 
'''
assert get_pell(4) == 12
assert get_pell(7) == 169
assert get_pell(8) == 408
