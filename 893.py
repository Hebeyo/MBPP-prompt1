"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to get the last element of each sublist.
'''

def Extract(lst): 
    return [item[-1] for item in lst]

'''
Standard answer: 
def Extract(lst): 
    return [item[-1] for item in lst] 
'''
assert Extract([[1, 2, 3], [4, 5], [6, 7, 8, 9]]) == [3, 5, 9]
assert Extract([['x', 'y', 'z'], ['m'], ['a', 'b'], ['u', 'v']]) == ['z', 'm', 'b', 'v']
assert Extract([[1, 2, 3], [4, 5]]) == [3, 5]
