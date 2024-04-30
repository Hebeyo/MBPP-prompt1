"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether the given list contains consecutive numbers or not.
'''

def check_Consecutive(l): 
    return sorted(l) == list(range(min(l),max(l)+1))

'''
Standard answer: 
def check_Consecutive(l): 
    return sorted(l) == list(range(min(l),max(l)+1)) 
'''
assert check_Consecutive([1,2,3,4,5]) == True
assert check_Consecutive([1,2,3,5,6]) == False
assert check_Consecutive([1,2,1]) == False
