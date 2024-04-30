"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find area of a sector.
'''

def sector_area(r,a):
    pi=22/7
    if a >= 360:
        return None
    sectorarea = (pi*r**2) * (a/360)
    return sectorarea

'''
Standard answer: 
def sector_area(r,a):
    pi=22/7
    if a >= 360:
        return None
    sectorarea = (pi*r**2) * (a/360)
    return sectorarea
'''
assert sector_area(4,45)==6.285714285714286
assert sector_area(9,45)==31.82142857142857
assert sector_area(9,360)==None
