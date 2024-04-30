"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to print duplicants from a list of integers.
'''

def Repeat(x):
    repeated = [] 
    for i in range(len(x)): 
        for j in range(i+1, len(x)): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated

'''
Standard answer: 
def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 
'''
assert Repeat([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]) == [20, 30, -20, 60]
assert Repeat([-1, 1, -1, 8]) == [-1]
assert Repeat([1, 2, 3, 1, 2,]) == [1, 2]
