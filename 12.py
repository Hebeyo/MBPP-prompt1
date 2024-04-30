"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to sort a given matrix in ascending order according to the sum of its rows.
'''

def sort_matrix(M):
    result = []
    for i in range(len(M)):
        result.append(sum(M[i]))
    for i in range(len(M)):
        for j in range(i+1,len(M)):
            if result[i] > result[j]:
                result[i],result[j] = result[j],result[i]
                M[i],M[j] = M[j],M[i]
    return M

'''
Standard answer: 
def sort_matrix(M):
    result = sorted(M, key=sum)
    return result
'''
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]
