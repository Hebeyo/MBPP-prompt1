"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count the number of integral co-ordinates that lie inside a square.
'''

def count_Intgral_Points(x1,y1,x2,y2):
    return ((y2 - y1 - 1) * (x2 - x1 - 1))

'''
Standard answer: 
def count_Intgral_Points(x1,y1,x2,y2): 
    return ((y2 - y1 - 1) * (x2 - x1 - 1)) 
'''
assert count_Intgral_Points(1,1,4,4) == 4
assert count_Intgral_Points(1,2,1,2) == 1
assert count_Intgral_Points(4,2,6,4) == 1
