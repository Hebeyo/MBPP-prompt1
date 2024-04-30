"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count the occcurences of an element in a tuple.
'''

def count_X(tup, x): 
    count = 0
    for ele in tup: 
        if (ele == x): 
            count = count + 1
    return count

'''
Standard answer: 
def count_X(tup, x): 
    count = 0
    for ele in tup: 
        if (ele == x): 
            count = count + 1
    return count 
'''
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10) == 3
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8) == 4
