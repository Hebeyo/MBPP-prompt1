"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find modulo division of two lists using map and lambda function.
'''

def moddiv_list(nums1,nums2):
  result = []
  for i in range(len(nums1)):
    result.append(nums1[i] % nums2[i])
  return result


'''
Standard answer: 
def moddiv_list(nums1,nums2):
  result = map(lambda x, y: x % y, nums1, nums2)
  return list(result)
'''
assert moddiv_list([4,5,6],[1, 2, 3])==[0, 1, 0]
assert moddiv_list([3,2],[1,4])==[0, 2]
assert moddiv_list([90,120],[50,70])==[40, 50]
