"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find k number of operations required to make all elements equal.
'''

def min_Ops(arr,n,k): 
    max1 = arr[0] 
    res = 0
    for i in range(1,n): 
        if (arr[i] > max1): 
            max1 = arr[i] 
    for i in range(0,n):  
        if ((max1 - arr[i]) % k != 0): 
            return -1 
        else: 
            res += (max1 - arr[i]) / k 
    return int(res)

'''
Standard answer: 
def min_Ops(arr,n,k): 
    max1 = max(arr) 
    res = 0
    for i in range(0,n):  
        if ((max1 - arr[i]) % k != 0): 
            return -1 
        else: 
            res += (max1 - arr[i]) / k 
    return int(res) 
'''
assert min_Ops([2,2,2,2],4,3) == 0
assert min_Ops([4,2,6,8],4,3) == -1
assert min_Ops([21,33,9,45,63],5,6) == 24
