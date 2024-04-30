"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the median of three specific numbers.
'''

def median_numbers(a,b,c):
  if a>b:
    if a<c:
      return a
    elif b>c:
      return b
    else:
      return c
  else:
    if a>c:
      return a
    elif b<c:
      return b
    else:
      return c

'''
Standard answer: 
def median_numbers(a,b,c):
 if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
 return median
'''
assert median_numbers(25,55,65)==55.0
assert median_numbers(20,10,30)==20.0
assert median_numbers(15,45,75)==45.0
