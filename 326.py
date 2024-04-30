"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to get the word with most number of occurrences in the given strings list.
'''

def most_occurrences(test_list):
  temp = {}
  for sub in test_list:
    for wrd in sub.split():
      if wrd in temp:
        temp[wrd] += 1
      else:
        temp[wrd] = 1
  max = 0
  for k, v in temp.items():
    if v > max:
      max = v
      res = k
  return (str(res))

'''
Standard answer: 
from collections import defaultdict 

def most_occurrences(test_list):
  temp = defaultdict(int)
  for sub in test_list:
    for wrd in sub.split():
      temp[wrd] += 1
  res = max(temp, key=temp.get)
  return (str(res)) 
'''
assert most_occurrences(["UTS is best for RTF", "RTF love UTS", "UTS is best"] ) == 'UTS'
assert most_occurrences(["Its been a great year", "this year is so worse", "this year is okay"] ) == 'year'
assert most_occurrences(["Families can be reunited", "people can be reunited", "Tasks can be achieved "] ) == 'can'
