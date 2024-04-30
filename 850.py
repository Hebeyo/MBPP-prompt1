"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check if a triangle of positive area is possible with the given angles.
'''

def is_triangleexists(a,b,c):
    if(a == 0 or b == 0 or c == 0 or (a + b + c)!= 180):
        return False
    if((a + b)< c or (b + c)< a or (a + c)< b):
        return False
    return True

'''
Standard answer: 
def is_triangleexists(a,b,c): 
    if(a != 0 and b != 0 and c != 0 and (a + b + c)== 180): 
        if((a + b)>= c or (b + c)>= a or (a + c)>= b): 
            return True 
        else:
            return False
    else:
        return False
'''
assert is_triangleexists(50,60,70)==True
assert is_triangleexists(90,45,45)==True
assert is_triangleexists(150,30,70)==False
