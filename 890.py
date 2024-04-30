"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the index of an extra element present in one sorted array.
'''

def find_Extra(arr1,arr2,n) : 
    for i in range(0, n) : 
        if (arr1[i] != arr2[i]) : 
            return i 
    return n

'''
Standard answer: 
def find_Extra(arr1,arr2,n) : 
    for i in range(0, n) : 
        if (arr1[i] != arr2[i]) : 
            return i 
    return n 
'''
assert find_Extra([1,2,3,4],[1,2,3],3) == 3
assert find_Extra([2,4,6,8,10],[2,4,6,8],4) == 4
assert find_Extra([1,3,5,7,9,11],[1,3,5,7,9],5) == 5
