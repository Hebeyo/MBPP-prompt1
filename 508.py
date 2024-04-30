"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check if the common elements between two given lists are in the same order or not.
'''

def same_order(l1, l2):
    common_elements = []
    for e1 in l1:
        if e1 in l2:
            common_elements.append(e1)
    return common_elements==[e for e in l2 if e in common_elements]

'''
Standard answer: 
def same_order(l1, l2):
    common_elements = set(l1) & set(l2)
    l1 = [e for e in l1 if e in common_elements]
    l2 = [e for e in l2 if e in common_elements]
    return l1 == l2
'''
assert same_order(["red","green","black","orange"],["red","pink","green","white","black"])==True
assert same_order(["red","pink","green","white","black"],["white","orange","pink","black"])==False
assert same_order(["red","green","black","orange"],["red","pink","green","white","black"])==True
