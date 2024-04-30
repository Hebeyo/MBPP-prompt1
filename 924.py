"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find maximum of two numbers.
'''

def max_of_two(x, y):
    return x if x > y else y

'''
Standard answer: 
def max_of_two( x, y ):
    if x > y:
        return x
    return y
'''
assert max_of_two(10,20)==20
assert max_of_two(19,15)==19
assert max_of_two(-10,-20)==-10
