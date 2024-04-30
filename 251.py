"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to insert an element before each element of a list.
'''

def insert_element(list,element):
    new_list = []
    for i in range(len(list)):
        new_list.append(element)
        new_list.append(list[i])
    return new_list

'''
Standard answer: 
def insert_element(list,element):
 list = [v for elt in list for v in (element, elt)]
 return list
'''
assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black'] 
assert insert_element(['python', 'java'] ,'program')==['program', 'python', 'program', 'java'] 
assert insert_element(['happy', 'sad'] ,'laugh')==['laugh', 'happy', 'laugh', 'sad'] 
