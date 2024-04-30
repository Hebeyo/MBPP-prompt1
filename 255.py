"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to choose specified number of colours from three different colours and generate all the combinations with repetitions.
'''

from itertools import combinations_with_replacement
def combinations_colors(l, n):
    return list(combinations_with_replacement(l,n))

'''
Standard answer: 
from itertools import combinations_with_replacement 
def combinations_colors(l, n):
    return list(combinations_with_replacement(l,n))
'''
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
assert combinations_colors( ["Red","Green","Blue"],2)==[('Red', 'Red'), ('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Green'), ('Green', 'Blue'), ('Blue', 'Blue')]
assert combinations_colors( ["Red","Green","Blue"],3)==[('Red', 'Red', 'Red'), ('Red', 'Red', 'Green'), ('Red', 'Red', 'Blue'), ('Red', 'Green', 'Green'), ('Red', 'Green', 'Blue'), ('Red', 'Blue', 'Blue'), ('Green', 'Green', 'Green'), ('Green', 'Green', 'Blue'), ('Green', 'Blue', 'Blue'), ('Blue', 'Blue', 'Blue')]
