"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to compute the sum of digits of each number of a given list.
'''

def sum_of_digits(nums):
  sum = 0
  for n in nums:
    for el in str(n):
      if el.isdigit():
        sum += int(el)
  return sum

'''
Standard answer: 
def sum_of_digits(nums):
    return sum(int(el) for n in nums for el in str(n) if el.isdigit())
'''
assert sum_of_digits([10,2,56])==14
assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
assert sum_of_digits([10,20,-4,5,-70])==19
