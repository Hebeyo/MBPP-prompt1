"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the vertex of a parabola.
'''

def parabola_vertex(a,b,c):
  return (-b/(2*a), (4*a*c - b**2)/(4*a))

'''
Standard answer: 
def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex
'''
assert parabola_vertex(5,3,2)==(-0.3, 1.55)
assert parabola_vertex(9,8,4)==(-0.4444444444444444, 2.2222222222222223)
assert parabola_vertex(2,4,6)==(-1.0, 4.0)
