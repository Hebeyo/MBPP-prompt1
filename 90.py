"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the length of the longest word.
'''

def len_log(list1):
    max = 0
    for i in list1:
        if len(i) > max:
            max = len(i)
    return max

'''
Standard answer: 
def len_log(list1):
    max=len(list1[0])
    for i in list1:
        if len(i)>max:
            max=len(i)
    return max
'''
assert len_log(["python","PHP","bigdata"]) == 7
assert len_log(["a","ab","abc"]) == 3
assert len_log(["small","big","tall"]) == 5
