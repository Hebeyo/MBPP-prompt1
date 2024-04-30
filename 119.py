"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the element that appears only once in a sorted array.
'''

def search(arr,n) :
    for i in range(n) :
        j = 0
        while j < n :
            if i != j :
                if arr[i] == arr[j] :
                    break
            j += 1
        if j == n :
            return arr[i]
    return -1

'''
Standard answer: 
def search(arr,n) :
    XOR = 0
    for i in range(n) :
        XOR = XOR ^ arr[i]
    return (XOR)
'''
assert search([1,1,2,2,3],5) == 3
assert search([1,1,3,3,4,4,5,5,7,7,8],11) == 8
assert search([1,2,2,3,3,4,4],7) == 1
