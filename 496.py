"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the smallest integers from a given list of numbers using heap queue algorithm.
'''

import heapq as hq
def heap_queue_smallest(nums,n):
  smallest_nums = hq.nsmallest(n, nums)
  return smallest_nums

'''
Standard answer: 
import heapq as hq
def heap_queue_smallest(nums,n):
  smallest_nums = hq.nsmallest(n, nums)
  return smallest_nums
'''
assert heap_queue_smallest( [25, 35, 22, 85, 14, 65, 75, 25, 58],3)==[14, 22, 25] 
assert heap_queue_smallest( [25, 35, 22, 85, 14, 65, 75, 25, 58],2)==[14, 22]
assert heap_queue_smallest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[14, 22, 22, 25, 35]
