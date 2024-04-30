"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the largest product of the pair of adjacent elements from a given list of integers.
'''

def adjacent_num_product(list_nums):
    max_product = 0
    for i in range(len(list_nums) - 1):
        product = list_nums[i] * list_nums[i + 1]
        if product > max_product:
            max_product = product
    return max_product


'''
Standard answer: 
def adjacent_num_product(list_nums):
    return max(a*b for a, b in zip(list_nums, list_nums[1:]))
'''
assert adjacent_num_product([1,2,3,4,5,6]) == 30
assert adjacent_num_product([1,2,3,4,5]) == 20
assert adjacent_num_product([2,3]) == 6
