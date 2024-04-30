"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check if a nested list is a subset of another nested list.
'''

def check_subset(list1,list2): 
    return all(map(list1.__contains__,list2))

'''
Standard answer: 
def check_subset(list1,list2): 
    return all(map(list1.__contains__,list2)) 
'''
assert check_subset([[1, 3], [5, 7], [9, 11], [13, 15, 17]] ,[[1, 3],[13,15,17]])==True
assert check_subset([[1, 2], [2, 3], [3, 4], [5, 6]],[[3, 4], [5, 6]])==True
assert check_subset([[[1, 2], [2, 3]], [[3, 4], [5, 7]]],[[[3, 4], [5, 6]]])==False
