"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the sublist having maximum length.
'''

def Find_Max(lst):
    maxList = max((x) for x in lst)
    return maxList

'''
Standard answer: 
def Find_Max(lst): 
    maxList = max((x) for x in lst) 
    return maxList
'''
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
assert Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]
assert Find_Max([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]
