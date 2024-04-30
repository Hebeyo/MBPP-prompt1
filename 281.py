"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check if the elements of a given list are unique or not.
'''

def all_unique(test_list):
    unique_list = []
    for i in test_list:
        if i in unique_list:
            return False
        else:
            unique_list.append(i)
    return True

'''
Standard answer: 
def all_unique(test_list):
    if len(test_list) > len(set(test_list)):
        return False
    return True
'''
assert all_unique([1,2,3]) == True
assert all_unique([1,2,1,2]) == False
assert all_unique([1,2,3,4,5]) == True
