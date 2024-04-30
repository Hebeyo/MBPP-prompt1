"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the minimum total path sum in the given triangle.
'''

def min_sum_path(A): 
	memo = [None] * len(A) 
	n = len(A) - 1
	for i in range(len(A[n])): 
		memo[i] = A[n][i] 
	for i in range(len(A) - 2, -1,-1): 
		for j in range( len(A[i])): 
			memo[j] = A[i][j] + min(memo[j], 
									memo[j + 1]) 
	return memo[0]

'''
Standard answer: 
def min_sum_path(A): 
	memo = [None] * len(A) 
	n = len(A) - 1
	for i in range(len(A[n])): 
		memo[i] = A[n][i] 
	for i in range(len(A) - 2, -1,-1): 
		for j in range( len(A[i])): 
			memo[j] = A[i][j] + min(memo[j], 
									memo[j + 1]) 
	return memo[0]
'''
assert min_sum_path([[ 2 ], [3, 9 ], [1, 6, 7 ]]) == 6
assert min_sum_path([[ 2 ], [3, 7 ], [8, 5, 6 ]]) == 10 
assert min_sum_path([[ 3 ], [6, 4 ], [5, 2, 7 ]]) == 9
