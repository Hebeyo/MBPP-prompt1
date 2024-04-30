"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the fixed point in the given array.
'''

def find_fixed_point(arr, n): 
	for i in range(n): 
		if arr[i] == i: 
			return i 
	return -1

'''
Standard answer: 
def find_fixed_point(arr, n): 
	for i in range(n): 
		if arr[i] is i: 
			return i 
	return -1
'''
assert find_fixed_point([-10, -1, 0, 3, 10, 11, 30, 50, 100],9) == 3
assert find_fixed_point([1, 2, 3, 4, 5, 6, 7, 8],8) == -1
assert find_fixed_point([0, 2, 5, 8, 17],5) == 0
