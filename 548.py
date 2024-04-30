"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the length of the longest increasing subsequence of the given sequence.
'''

def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1]*n
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
    maximum = 0
    for i in range(n):
        maximum = max(maximum , lis[i])
    return maximum

'''
Standard answer: 
def longest_increasing_subsequence(arr): 
	n = len(arr) 
	longest_increasing_subsequence = [1]*n 
	for i in range (1 , n): 
		for j in range(0 , i): 
			if arr[i] > arr[j] and longest_increasing_subsequence[i]< longest_increasing_subsequence[j] + 1 : 
				longest_increasing_subsequence[i] = longest_increasing_subsequence[j]+1
	maximum = 0
	for i in range(n): 
		maximum = max(maximum , longest_increasing_subsequence[i]) 
	return maximum
'''
assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60]) == 5
assert longest_increasing_subsequence([3, 10, 2, 1, 20]) == 3
assert longest_increasing_subsequence([50, 3, 10, 7, 40, 80]) == 4 
