"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether every odd index contains odd numbers of a given list.
'''

def odd_position(nums):
	for i in range(len(nums)):
		if nums[i] % 2 == 0 and i % 2 != 0:
			return False
		if nums[i] % 2 != 0 and i % 2 == 0:
			return False
	return True

'''
Standard answer: 
def odd_position(nums):
	return all(nums[i]%2==i%2 for i in range(len(nums)))
'''
assert odd_position([2,1,4,3,6,7,6,3]) == True
assert odd_position([4,1,2]) == True
assert odd_position([1,2,3]) == False
