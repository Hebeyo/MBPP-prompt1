"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function of recursion list sum.
'''

def recursive_list_sum(data_list):
	sum = 0
	for element in data_list:
		if type(element) == type([]):
			sum = sum + recursive_list_sum(element)
		else:
			sum = sum + element
	return sum

'''
Standard answer: 
def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element
	return total
'''
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
assert recursive_list_sum(([7, 10, [15,14],[19,41]]))==106
assert recursive_list_sum(([10, 20, [30,40],[50,60]]))==210
