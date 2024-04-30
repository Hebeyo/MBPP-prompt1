"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the frequency of the largest value in a given array.
'''

def frequency_Of_Largest(n,arr):
    max_num = max(arr)
    return arr.count(max_num)

'''
Standard answer: 
def frequency_Of_Largest(n,arr): 
    mn = arr[0] 
    freq = 1
    for i in range(1,n): 
        if (arr[i] >mn): 
            mn = arr[i] 
            freq = 1
        elif (arr[i] == mn): 
            freq += 1
    return freq 
'''
assert frequency_Of_Largest(5,[1,2,3,4,4]) == 2
assert frequency_Of_Largest(3,[5,6,5]) == 1
assert frequency_Of_Largest(4,[2,7,7,7]) == 3
