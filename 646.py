"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count number of cubes of size k in a cube of size n.
'''

def No_of_cubes(N,K):
    No = 0
    for i in range(N-K+1):
        for j in range(N-K+1):
            for k in range(N-K+1):
                No += 1
    return No

'''
Standard answer: 
def No_of_cubes(N,K):
    No = 0
    No = (N - K + 1)
    No = pow(No, 3)
    return No
'''
assert No_of_cubes(2,1) == 8
assert No_of_cubes(5,2) == 64
assert No_of_cubes(1,1) == 1
