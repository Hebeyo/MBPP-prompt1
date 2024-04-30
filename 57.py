"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the largest number that can be formed with the given digits.
'''

def find_Max_Num(arr,n) : 
    for i in range(n): 
        for j in range(n-i-1) : 
            if arr[j] < arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    num = 0
    for i in range(n) : 
        num = num * 10 + arr[i] 
    return num

'''
Standard answer: 
def find_Max_Num(arr,n) : 
    arr.sort(reverse = True) 
    num = arr[0] 
    for i in range(1,n) : 
        num = num * 10 + arr[i] 
    return num 
'''
assert find_Max_Num([1,2,3],3) == 321
assert find_Max_Num([4,5,6,1],4) == 6541
assert find_Max_Num([1,2,3,9],4) == 9321
