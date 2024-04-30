"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the greatest common divisor (gcd) of two integers by using recursion.
'''

def recur_gcd(a, b):
	if b == 0:
		return a
	else:
		return recur_gcd(b, a%b)

'''
Standard answer: 
def recur_gcd(a, b):
	low = min(a, b)
	high = max(a, b)
	if low == 0:
		return high
	elif low == 1:
		return 1
	else:
		return recur_gcd(low, high%low)
'''
assert recur_gcd(12,14) == 2
assert recur_gcd(13,17) == 1
assert recur_gcd(9, 3) == 3
