"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the average of a list.
'''

def Average(lst): 
    return sum(lst) / len(lst)

'''
Standard answer: 
def Average(lst): 
    return sum(lst) / len(lst) 
'''
assert Average([15, 9, 55, 41, 35, 20, 62, 49]) == 35.75
assert Average([4, 5, 1, 2, 9, 7, 10, 8]) == 5.75
assert Average([1,2,3]) == 2
