"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the sum of xor of all pairs of numbers in the given array.
'''

def pair_OR_Sum(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans

'''
Standard answer: 
def pair_OR_Sum(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
'''
assert pair_OR_Sum([5,9,7,6],4) == 47
assert pair_OR_Sum([7,3,5],3) == 12
assert pair_OR_Sum([7,3],2) == 4
