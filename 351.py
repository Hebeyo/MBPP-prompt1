"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the first element occurring k times in a given array.
'''

def first_Element(arr,n,k): 
    count_map = {}; 
    for i in range(0, n): 
        if(arr[i] in count_map.keys()): 
            count_map[arr[i]] += 1
        else: 
            count_map[arr[i]] = 1
        i += 1
    for i in range(0, n):  
        if (count_map[arr[i]] == k): 
            return arr[i] 
        i += 1 
    return -1

'''
Standard answer: 
def first_Element(arr,n,k): 
    count_map = {}; 
    for i in range(0, n): 
        if(arr[i] in count_map.keys()): 
            count_map[arr[i]] += 1
        else: 
            count_map[arr[i]] = 1
        i += 1
    for i in range(0, n):  
        if (count_map[arr[i]] == k): 
            return arr[i] 
        i += 1 
    return -1
'''
assert first_Element([0,1,2,3,4,5],6,1) == 0
assert first_Element([1,2,1,3,4],5,2) == 1
assert first_Element([2,3,4,3,5,7,1,2,3,5],10,2) == 2
