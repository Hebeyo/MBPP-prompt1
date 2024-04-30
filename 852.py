"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to remove negative numbers from a list.
'''

def remove_negs(num_list): 
    return [item for item in num_list if item >= 0]

'''
Standard answer: 
def remove_negs(num_list): 
    for item in num_list: 
        if item < 0: 
           num_list.remove(item) 
    return num_list
'''
assert remove_negs([1,-2,3,-4]) == [1,3]
assert remove_negs([1,2,3,-4]) == [1,2,3]
assert remove_negs([4,5,-6,7,-8]) == [4,5,7]
