"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the n’th carol number.
'''

def get_carol(n):
    return (2 ** n - 1) ** 2 - 2

'''
Standard answer: 
def get_carol(n): 
	result = (2**n) - 1
	return result * result - 2
'''
assert get_carol(2) == 7
assert get_carol(4) == 223
assert get_carol(5) == 959
