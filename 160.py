"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find x and y that satisfies ax + by = n.
'''

def solution(a, b, n):
    for i in range(n//a + 1):
        if (n - i * a) % b == 0:
            return ('x = ', i, ', y = ', (n - i * a) // b)
    return 'No solution'

'''
Standard answer: 
def solution (a, b, n): 
	i = 0
	while i * a <= n: 
		if (n - (i * a)) % b == 0: 
			return ("x = ",i ,", y = ", 
			int((n - (i * a)) / b)) 
			return 0
		i = i + 1
	return ("No solution") 
'''
assert solution(2, 3, 7) == ('x = ', 2, ', y = ', 1)
assert solution(4, 2, 7) == 'No solution'
assert solution(1, 13, 17) == ('x = ', 4, ', y = ', 1)
