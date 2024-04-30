"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the depth of a dictionary.
'''

def dict_depth(d):
    if isinstance(d, dict):
        depth = 0
        for key in d:
            depth = max(depth, dict_depth(d[key]))
        return depth + 1
    else:
        return 0

'''
Standard answer: 
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0
'''
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c':'python'}})==2
assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3
