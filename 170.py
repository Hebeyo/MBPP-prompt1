"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find sum of the numbers in a list between the indices of a specified range.
'''

def sum_range_list(list1,m,n):
    sum_range = 0
    for i in range(m,n+1):
        sum_range += list1[i]
    return sum_range

'''
Standard answer: 
def sum_range_list(list1, m, n):                                                                                                                                                                                                
    sum_range = 0                                                                                                                                                                                                         
    for i in range(m, n+1, 1):                                                                                                                                                                                        
        sum_range += list1[i]                                                                                                                                                                                                  
    return sum_range   
'''
assert sum_range_list( [2,1,5,6,8,3,4,9,10,11,8,12],8,10)==29
assert sum_range_list( [2,1,5,6,8,3,4,9,10,11,8,12],5,7)==16
assert sum_range_list( [2,1,5,6,8,3,4,9,10,11,8,12],7,10)==38
