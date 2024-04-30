"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to interchange the first and last elements in a list.
'''

def swap_List(newList): 
    temp = newList[0] 
    newList[0] = newList[-1] 
    newList[-1] = temp  
    return newList

'''
Standard answer: 
def swap_List(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp  
    return newList 
'''
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
assert swap_List([1, 2, 3]) == [3, 2, 1]
assert swap_List([4, 5, 6]) == [6, 5, 4]
