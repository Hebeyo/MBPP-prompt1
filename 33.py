"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to convert a decimal number to binary number.
'''

def decimal_To_Binary(N):
    B_Number = 0
    cnt = 0
    while (N != 0):
        rem = N % 2
        c = 10**cnt
        B_Number += rem*c
        N //= 2
        cnt += 1
    return B_Number


'''
Standard answer: 
def decimal_To_Binary(N): 
    B_Number = 0
    cnt = 0
    while (N != 0): 
        rem = N % 2
        c = pow(10,cnt)  
        B_Number += rem*c  
        N //= 2 
        cnt += 1
    return B_Number  
'''
assert decimal_To_Binary(10) == 1010
assert decimal_To_Binary(1) == 1
assert decimal_To_Binary(20) == 10100
