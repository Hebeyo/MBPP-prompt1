"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to locate the left insertion point for a specified value in sorted order.
'''

def left_insertion(a, x):
    left = 0
    right = len(a)
    while left < right:
        mid = left + (right - left) // 2
        if a[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

'''
Standard answer: 
import bisect
def left_insertion(a, x):
    i = bisect.bisect_left(a, x)
    return i
'''
assert left_insertion([1,2,4,5],6)==4
assert left_insertion([1,2,4,5],3)==2
assert left_insertion([1,2,4,5],7)==4
