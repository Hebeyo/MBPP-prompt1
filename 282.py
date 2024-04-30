"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to substaract two lists using map and lambda function.
'''

def sub_list(nums1,nums2):
  result = []
  for i in range(len(nums1)):
    result.append(nums1[i]-nums2[i])
  return result

'''
Standard answer: 
def sub_list(nums1,nums2):
  result = map(lambda x, y: x - y, nums1, nums2)
  return list(result)
'''
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
assert sub_list([1,2],[3,4])==[-2,-2]
assert sub_list([90,120],[50,70])==[40,50]
