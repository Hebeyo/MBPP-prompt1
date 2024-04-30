"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the n - cheap price items from a given dataset using heap queue algorithm.
'''

def cheap_items(items, n):
  import heapq
  return heapq.nsmallest(n, items, key=lambda s: s['price'])

'''
Standard answer: 
import heapq
def cheap_items(items,n):
  cheap_items = heapq.nsmallest(n, items, key=lambda s: s['price'])
  return cheap_items
'''
assert cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-1', 'price': 101.1}]
assert cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],2)==[{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}]
assert cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-4', 'price': 22.75}]
