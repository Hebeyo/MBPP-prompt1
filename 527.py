"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find all pairs in an integer array whose sum is equal to a given number.
'''

def get_pairs_count(arr, n, sum):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count

'''
Standard answer: 
def get_pairs_count(arr, n, sum):
    count = 0 
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count
'''
assert get_pairs_count([1, 5, 7, -1, 5], 5, 6) == 3
assert get_pairs_count([1, 5, 7, -1], 4, 6) == 2
assert get_pairs_count([1, 1, 1, 1], 4, 2) == 6
