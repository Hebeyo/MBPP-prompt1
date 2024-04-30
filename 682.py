"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to multiply two lists using map and lambda function.
'''

def mul_list(nums1,nums2):
  result = []
  for i in range(len(nums1)):
    result.append(nums1[i]*nums2[i])
  return result

'''
Standard answer: 
def mul_list(nums1,nums2):
  result = map(lambda x, y: x * y, nums1, nums2)
  return list(result)
'''
assert mul_list([1, 2, 3],[4,5,6])==[4,10,18]
assert mul_list([1,2],[3,4])==[3,8]
assert mul_list([90,120],[50,70])==[4500,8400]
