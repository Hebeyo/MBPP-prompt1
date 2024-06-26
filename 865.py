"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to print n-times a list using map function.
'''

def ntimes_list(nums,n):
    result = []
    for i in nums:
        result.append(i*n)
    return result

'''
Standard answer: 
def ntimes_list(nums,n):
    result = map(lambda x:n*x, nums) 
    return list(result)
'''
assert ntimes_list([1, 2, 3, 4, 5, 6, 7],3)==[3, 6, 9, 12, 15, 18, 21]
assert ntimes_list([1, 2, 3, 4, 5, 6, 7],4)==[4, 8, 12, 16, 20, 24, 28]
assert ntimes_list([1, 2, 3, 4, 5, 6, 7],10)==[10, 20, 30, 40, 50, 60, 70]
