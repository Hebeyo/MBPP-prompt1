"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the difference between highest and least frequencies in a given array.
'''

def find_Diff(arr,n):
    my_dict = {}
    for i in arr:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    max_count = 0
    min_count = n
    for key in my_dict:
        if my_dict[key] > max_count:
            max_count = my_dict[key]
        if my_dict[key] < min_count:
            min_count = my_dict[key]
    return max_count - min_count


'''
Standard answer: 
def find_Diff(arr,n): 
    arr.sort()  
    count = 0; max_count = 0; min_count = n 
    for i in range(0,(n-1)): 
        if arr[i] == arr[i + 1]: 
            count += 1
            continue
        else: 
            max_count = max(max_count,count) 
            min_count = min(min_count,count) 
            count = 0
    return max_count - min_count 
'''
assert find_Diff([1,1,2,2,7,8,4,5,1,4],10) == 2
assert find_Diff([1,7,9,2,3,3,1,3,3],9) == 3
assert find_Diff([1,2,1,2],4) == 0
