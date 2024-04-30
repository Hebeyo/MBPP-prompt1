"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the longest common prefix in the given set of strings.
'''

def common_prefix(arr, n):
    if n == 0:
        return ""
    if n == 1:
        return arr[0]
    arr.sort()
    end = min(len(arr[0]), len(arr[n - 1]))
    i = 0
    while (i < end and arr[0][i] == arr[n - 1][i]):
        i += 1
    pre = arr[0][:i]
    return pre


'''
Standard answer: 
def common_prefix_util(str1, str2): 
	result = ""; 
	n1 = len(str1) 
	n2 = len(str2) 
	i = 0
	j = 0
	while i <= n1 - 1 and j <= n2 - 1: 
		if (str1[i] != str2[j]): 
			break
		result += str1[i] 
		i += 1
		j += 1
	return (result) 
def common_prefix (arr, n): 
	prefix = arr[0] 
	for i in range (1, n): 
		prefix = common_prefix_util(prefix, arr[i]) 
	return (prefix) 
'''
assert common_prefix(["tablets", "tables", "taxi", "tamarind"], 4) == 'ta'
assert common_prefix(["apples", "ape", "april"], 3) == 'ap'
assert common_prefix(["teens", "teenager", "teenmar"], 3) == 'teen'
