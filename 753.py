"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find minimum k records from tuple list.
'''

def min_k(test_list, K):
  res = []
  for i in range(K):
    res.append(sorted(test_list, key = lambda x: x[1])[i])
  return (res)

'''
Standard answer: 
def min_k(test_list, K):
  res = sorted(test_list, key = lambda x: x[1])[:K]
  return (res) 
'''
assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
assert min_k([('Sanjeev', 11), ('Angat', 5), ('Akash', 3), ('Nepin', 9)], 3) == [('Akash', 3), ('Angat', 5), ('Nepin', 9)]
assert min_k([('tanmay', 14), ('Amer', 11), ('Ayesha', 9), ('SKD', 16)], 1) == [('Ayesha', 9)]
