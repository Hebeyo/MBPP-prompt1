"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the maximum value in a given heterogeneous list.
'''

def max_val(listval):
    max_val = 0
    for i in listval:
        if isinstance(i, int):
            if i > max_val:
                max_val = i
    return(max_val)

'''
Standard answer: 
def max_val(listval):
     max_val = max(i for i in listval if isinstance(i, int)) 
     return(max_val)
'''
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
assert max_val(['Python', 15, 20, 25])==25
assert max_val(['Python', 30, 20, 40, 50, 'version'])==50
