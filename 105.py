"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count true booleans in the given list.
'''


def count(lst):   
    count = 0
    for x in lst:
        if x == True:
            count += 1
    return count

'''
Standard answer: 
def count(lst):   
    return sum(lst) 
'''
assert count([True,False,True]) == 2
assert count([False,False]) == 0
assert count([True,True,True]) == 3
