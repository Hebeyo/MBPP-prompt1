"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the item with maximum frequency in a given list.
'''

def max_occurrences(nums):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    max_key = max(dict, key=dict.get)
    return (max_key, dict[max_key])

'''
Standard answer: 
from collections import defaultdict
def max_occurrences(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: x[1]) 
    return result
'''
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==(2, 5)
assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,16,18])==(8, 2)
assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==(20, 3)
