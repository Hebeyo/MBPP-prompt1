"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the directrix of a parabola.
'''

def parabola_directrix(a, b, c): 
  directrix=((int)(c - ((b * b) + 1) * 4 * a ))
  return directrix

'''
Standard answer: 
def parabola_directrix(a, b, c): 
  directrix=((int)(c - ((b * b) + 1) * 4 * a ))
  return directrix
'''
assert parabola_directrix(5,3,2)==-198
assert parabola_directrix(9,8,4)==-2336
assert parabola_directrix(2,4,6)==-130
