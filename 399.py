"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to perform the mathematical bitwise xor operation across the given tuples.
'''

def bitwise_xor(test_tup1, test_tup2):
  res = []
  for i in range(len(test_tup1)):
    res.append(test_tup1[i] ^ test_tup2[i])
  return tuple(res)

'''
Standard answer: 
def bitwise_xor(test_tup1, test_tup2):
  res = tuple(ele1 ^ ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res) 
'''
assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
assert bitwise_xor((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)
assert bitwise_xor((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13)
