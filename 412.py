"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to remove odd numbers from a given list.
'''

def remove_odd(l):
    return [i for i in l if i % 2 == 0]

'''
Standard answer: 
def remove_odd(l):
    for i in l:
        if i % 2 != 0:
            l.remove(i)
    return l
'''
assert remove_odd([1,2,3]) == [2]
assert remove_odd([2,4,6]) == [2,4,6]
assert remove_odd([10,20,3]) == [10,20]
