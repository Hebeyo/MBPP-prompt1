"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to combine two dictionaries by adding values for common keys.
'''

def add_dict(d1,d2):
    add_dict = {}
    for key in d1:
        if key in d2:
            add_dict[key] = d1[key] + d2[key]
        else:
            add_dict[key] = d1[key]
    for key in d2:
        if key not in add_dict:
            add_dict[key] = d2[key]
    return add_dict

'''
Standard answer: 
from collections import Counter
def add_dict(d1,d2):
   add_dict = Counter(d1) + Counter(d2)
   return add_dict
'''
assert add_dict({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400})==({'b': 400, 'd': 400, 'a': 400, 'c': 300}) 
assert add_dict({'a': 500, 'b': 700, 'c':900},{'a': 500, 'b': 600, 'd':900})==({'b': 1300, 'd': 900, 'a': 1000, 'c': 900}) 
assert add_dict({'a':900,'b':900,'d':900},{'a':900,'b':900,'d':900})==({'b': 1800, 'd': 1800, 'a': 1800})
