"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check whether a specified list is sorted or not.
'''

def issort_list(list1):
    result = True
    for i in range(len(list1)-1):
        if list1[i] > list1[i+1]:
            result = False
            break
    return result

'''
Standard answer: 
def issort_list(list1):
    result = all(list1[i] <= list1[i+1] for i in range(len(list1)-1))
    return result
'''
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
assert issort_list([1, 2, 4, 6, 8, 10, 12, 14, 20, 17])==False
assert issort_list([1, 2, 4, 6, 8, 10,15,14,20])==False
