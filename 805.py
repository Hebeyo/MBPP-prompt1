"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the list in a list of lists whose sum of elements is the highest.
'''

def max_sum_list(lists):
    max_sum = 0
    max_list = []
    for list in lists:
        sum_list = sum(list)
        if sum_list > max_sum:
            max_sum = sum_list
            max_list = list
    return max_list

'''
Standard answer: 
def max_sum_list(lists):
 return max(lists, key=sum)
'''
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12] 
assert max_sum_list([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10] 
assert max_sum_list([[2,3,1]])==[2,3,1] 
