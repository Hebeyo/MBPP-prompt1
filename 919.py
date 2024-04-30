"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to multiply all items in the list.
'''

def multiply_list(items):
    product = 1
    for i in items:
        product *= i
    return product

'''
Standard answer: 
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
'''
assert multiply_list([1,-2,3]) == -6
assert multiply_list([1,2,3,4]) == 24
assert multiply_list([3,1,2,3]) == 18
