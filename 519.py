"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to calculate volume of a tetrahedron.
'''

def volume_tetrahedron(num):
	return round(num ** 3 / (6 * 2 ** 0.5), 2)

'''
Standard answer: 
import math
def volume_tetrahedron(num):
	volume = (num ** 3 / (6 * math.sqrt(2)))	
	return round(volume, 2)
'''
assert volume_tetrahedron(10)==117.85
assert volume_tetrahedron(15)==397.75
assert volume_tetrahedron(20)==942.81
