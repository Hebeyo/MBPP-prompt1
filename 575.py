"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find nth number in a sequence which is not a multiple of a given number.
'''

def count_no(A,N,L,R): 
    count = 0
    i = L
    while count < N:
        if i % A != 0:
            count += 1
        i += 1
    return i - 1

'''
Standard answer: 
def count_no (A,N,L,R): 
    count = 0
    for i in range (L,R + 1): 
        if (i % A != 0): 
            count += 1
        if (count == N): 
            break
    return (i) 
'''
assert count_no(2,3,1,10) == 5
assert count_no(3,6,4,20) == 11
assert count_no(5,10,4,20) == 16
