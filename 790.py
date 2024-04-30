"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether every even index contains even numbers of a given list.
'''

def even_position(nums):
	for i in range(len(nums)):
		if (nums[i]%2==0 and i%2!=0) or (nums[i]%2!=0 and i%2==0):
			return False
	return True

'''
Standard answer: 
def even_position(nums):
	return all(nums[i]%2==i%2 for i in range(len(nums)))
'''
assert even_position([3,2,1]) == False
assert even_position([1,2,3]) == False
assert even_position([2,1,4]) == True
