"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to count number of lists in a given list of lists and square the count.
'''

def count_list(input_list):
    count = 0
    for i in input_list:
        count += 1
    return count**2

'''
Standard answer: 
def count_list(input_list): 
    return (len(input_list))**2
'''
assert count_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==25
assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]] )==16
assert count_list([[2, 4], [[6,8], [4,5,8]], [10, 12, 14]])==9
