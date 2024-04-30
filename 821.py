"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to merge two dictionaries into a single expression.
'''

def merge_dictionaries(dict1,dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

'''
Standard answer: 
import collections as ct
def merge_dictionaries(dict1,dict2):
    merged_dict = dict(ct.ChainMap({}, dict1, dict2))
    return merged_dict
'''
assert merge_dictionaries({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White'}
assert merge_dictionaries({ "R": "Red", "B": "Black", "P": "Pink" },{ "O": "Orange", "W": "White", "B": "Black" })=={'O': 'Orange', 'P': 'Pink', 'B': 'Black', 'W': 'White', 'R': 'Red'}
assert merge_dictionaries({ "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'W': 'White', 'O': 'Orange', 'G': 'Green', 'B': 'Black'}
