"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to extract the elementwise and tuples from the given two tuples.
'''

def and_tuples(test_tup1, test_tup2):
    res = []
    for i in range(len(test_tup1)):
        res.append(test_tup1[i] & test_tup2[i])
    return tuple(res)

'''
Standard answer: 
def and_tuples(test_tup1, test_tup2):
  res = tuple(ele1 & ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res) 
'''
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
assert and_tuples((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)
assert and_tuples((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0)
