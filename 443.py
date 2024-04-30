"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the largest negative number from the given list.
'''

def largest_neg(list1): 
    return min(list1)

'''
Standard answer: 
def largest_neg(list1): 
    max = list1[0] 
    for x in list1: 
        if x < max : 
             max = x  
    return max
'''
assert largest_neg([1,2,3,-4,-6]) == -6
assert largest_neg([1,2,3,-8,-9]) == -9
assert largest_neg([1,2,3,4,-1]) == -1
