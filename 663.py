"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the largest possible value of k such that k modulo x is y.
'''

def find_max_val(n, x, y):
    max_val = -1
    for k in range(n + 1):
        if (k % x == y):
            max_val = max(max_val, k)
    return max_val

'''
Standard answer: 
import sys 
def find_max_val(n, x, y): 
	ans = -sys.maxsize 
	for k in range(n + 1): 
		if (k % x == y): 
			ans = max(ans, k) 
	return (ans if (ans >= 0 and
					ans <= n) else -1) 
'''
assert find_max_val(15, 10, 5) == 15
assert find_max_val(187, 10, 5) == 185
assert find_max_val(16, 11, 1) == 12
