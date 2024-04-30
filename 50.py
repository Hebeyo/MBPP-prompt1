"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the list with minimum length using lambda function.
'''

def min_length_list(input_list):
    min_length = len(input_list[0])
    min_list = input_list[0]
    for i in input_list:
        if len(i)<min_length:
            min_length = len(i)
            min_list = i
    return(min_length, min_list)

'''
Standard answer: 
def min_length_list(input_list):
    min_length = min(len(x) for x in input_list )  
    min_list = min(input_list, key = lambda i: len(i))
    return(min_length, min_list)
'''
assert min_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(1, [0])
assert min_length_list([[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1]])==(1,[1])
assert min_length_list([[3,4,5],[6,7,8,9],[10,11,12],[1,2]])==(2,[1,2])
