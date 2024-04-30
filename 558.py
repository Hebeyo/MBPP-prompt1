"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the digit distance between two integers.
'''

def digit_distance_nums(n1, n2):
    n1 = str(n1)
    n2 = str(n2)
    if len(n1) > len(n2):
        n2 = '0'*(len(n1)-len(n2)) + n2
    elif len(n1) < len(n2):
        n1 = '0'*(len(n2)-len(n1)) + n1
    return sum([abs(int(n1[i])-int(n2[i])) for i in range(len(n1))])

'''
Standard answer: 
def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))
'''
assert digit_distance_nums(1,2) == 1
assert digit_distance_nums(23,56) == 6
assert digit_distance_nums(123,256) == 7
