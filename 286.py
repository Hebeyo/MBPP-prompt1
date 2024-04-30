"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the largest sum of contiguous array in the modified array which is formed by repeating the given array k times.
'''

def max_sub_array_sum_repeated(arr, n, k):
    if k == 1:
        max_so_far = -2147483648
        max_ending_here = 0
        for i in range(n):
            max_ending_here = max_ending_here + arr[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far
    else:
        max_so_far = -2147483648
        max_ending_here = 0
        for i in range(n * k):
            max_ending_here = max_ending_here + arr[i % n]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

'''
Standard answer: 
def max_sub_array_sum_repeated(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
'''
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1
