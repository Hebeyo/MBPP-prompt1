"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether a sequence of numbers has an increasing trend or not.
'''

def increasing_trend(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

'''
Standard answer: 
def increasing_trend(nums):
    if (sorted(nums)== nums):
        return True
    else:
        return False
'''
assert increasing_trend([1,2,3,4]) == True
assert increasing_trend([4,3,2,1]) == False
assert increasing_trend([0,1,4,9]) == True
