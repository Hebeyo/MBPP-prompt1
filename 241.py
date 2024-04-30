"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to generate a 3d array having each element as '*'.
'''

def array_3d(m,n,o):
    array_3d = [[ ['*' for col in range(m)] for col in range(n)] for row in range(o)]
    return array_3d

'''
Standard answer: 
def array_3d(m,n,o):
 array_3d = [[ ['*' for col in range(m)] for col in range(n)] for row in range(o)]
 return array_3d
'''
assert array_3d(6,4,3)==[[['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*']], [['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*']], [['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*']]]
assert array_3d(5,3,4)==[[['*', '*', '*', '*', '*'], ['*', '*', '*', '*','*'], ['*', '*', '*', '*', '*']], [['*', '*', '*', '*', '*'],['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']], [['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']], [['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*']]]
assert array_3d(1,2,3)==[[['*'],['*']],[['*'],['*']],[['*'],['*']]]
