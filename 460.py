"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to get the first element of each sublist.
'''

def Extract(lst): 
    return [item[0] for item in lst]

'''
Standard answer: 
def Extract(lst): 
    return [item[0] for item in lst] 
'''
assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
assert Extract([[1,2,3],[4, 5]]) == [1,4]
assert Extract([[9,8,1],[1,2]]) == [9,1]
