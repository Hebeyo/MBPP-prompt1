"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to perform the exponentiation of the given two tuples.
'''

def find_exponentio(test_tup1, test_tup2):
  res = []
  for i in range(len(test_tup1)):
    res.append(test_tup1[i]**test_tup2[i])
  return tuple(res)

'''
Standard answer: 
def find_exponentio(test_tup1, test_tup2):
  res = tuple(ele1 ** ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res)

'''
assert find_exponentio((10, 4, 5, 6), (5, 6, 7, 5)) == (100000, 4096, 78125, 7776)
assert find_exponentio((11, 5, 6, 7), (6, 7, 8, 6)) == (1771561, 78125, 1679616, 117649)
assert find_exponentio((12, 6, 7, 8), (7, 8, 9, 7)) == (35831808, 1679616, 40353607, 2097152)
