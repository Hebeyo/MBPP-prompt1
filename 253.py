"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count integers from a given list.
'''

def count_integer(list1):
    return len([i for i in list1 if isinstance(i, int)])

'''
Standard answer: 
def count_integer(list1):
    ctr = 0
    for i in list1:
        if isinstance(i, int):
            ctr = ctr + 1
    return ctr
'''
assert count_integer([1,2,'abc',1.2]) == 2
assert count_integer([1,2,3]) == 3
assert count_integer([1,1.2,4,5.1]) == 2
