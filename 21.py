"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find m number of multiples of n.
'''

def multiples_of_num(m,n):
    multiples_of_num= []
    for i in range(1,m+1):
        multiples_of_num.append(n*i)
    return multiples_of_num

'''
Standard answer: 
def multiples_of_num(m,n): 
    multiples_of_num= list(range(n,(m+1)*n, n)) 
    return list(multiples_of_num)
'''
assert multiples_of_num(4,3)== [3,6,9,12]
assert multiples_of_num(2,5)== [5,10]
assert multiples_of_num(9,2)== [2,4,6,8,10,12,14,16,18]
