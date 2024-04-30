"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to divide a number into two parts such that the sum of digits is maximum.
'''

def sum_digits_twoparts(N) : 
    A = 0
    for i in range(1, N): 
        A = A * 10 + 9
        if A > N: 
            A = A // 10
            break
    B = N - A
    sum1 = 0
    while A: 
        sum1 += A % 10
        A = A // 10
    sum2 = 0
    while B: 
        sum2 += B % 10
        B = B // 10
    return sum1 + sum2

'''
Standard answer: 
def sum_digits_single(x) : 
    ans = 0
    while x : 
        ans += x % 10
        x //= 10  
    return ans 
def closest(x) : 
    ans = 0
    while (ans * 10 + 9 <= x) : 
        ans = ans * 10 + 9  
    return ans   
def sum_digits_twoparts(N) : 
    A = closest(N)  
    return sum_digits_single(A) + sum_digits_single(N - A) 
'''
assert sum_digits_twoparts(35)==17
assert sum_digits_twoparts(7)==7
assert sum_digits_twoparts(100)==19
