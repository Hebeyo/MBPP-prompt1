"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to split a given list into two parts where the length of the first part of the list is given.
'''

def split_two_parts(list1, L):
    return list1[:L], list1[L:]

'''
Standard answer: 
def split_two_parts(list1, L):
    return list1[:L], list1[L:]
'''
assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
assert split_two_parts(['a', 'b', 'c', 'd'],2)==(['a', 'b'], ['c', 'd'])
assert split_two_parts(['p', 'y', 't', 'h', 'o', 'n'],4)==(['p', 'y', 't', 'h'], ['o', 'n'])
