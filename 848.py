"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the area of a trapezium.
'''

def area_trapezium(base1,base2,height):
    return 0.5 * (base1 + base2) * height

'''
Standard answer: 
def area_trapezium(base1,base2,height):
 area = 0.5 * (base1 + base2) * height
 return area
'''
assert area_trapezium(6,9,4)==30
assert area_trapezium(10,20,30)==450
assert area_trapezium(15,25,35)==700
