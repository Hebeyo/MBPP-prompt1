"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the largest integers from a given list of numbers using heap queue algorithm.
'''

def heap_queue_largest(nums, n):
    import heapq as hq
    hq.heapify(nums)
    largest_nums = hq.nlargest(n, nums)
    return largest_nums

'''
Standard answer: 
import heapq as hq
def heap_queue_largest(nums,n):
  largest_nums = hq.nlargest(n, nums)
  return largest_nums
'''
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65] 
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],2)==[85, 75] 
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]
