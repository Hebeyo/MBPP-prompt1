"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count the maximum number of equilateral triangles that can be formed within a given equilateral triangle.
'''

def No_of_Triangle(N,K):
    if (N < K):
        return -1;
    else:
        Tri_up = 0;
        Tri_up = ((N - K + 1) *(N - K + 2)) // 2;
        Tri_down = 0;
        Tri_down = ((N - 2 * K + 1) *(N - 2 * K + 2)) // 2;
        return Tri_up + Tri_down;



'''
Standard answer: 
def No_of_Triangle(N,K):
    if (N < K):
        return -1;
    else:
        Tri_up = 0;
        Tri_up = ((N - K + 1) *(N - K + 2)) // 2;
        Tri_down = 0;
        Tri_down = ((N - 2 * K + 1) *(N - 2 * K + 2)) // 2;
        return Tri_up + Tri_down;
'''
assert No_of_Triangle(4,2) == 7
assert No_of_Triangle(4,3) == 3
assert No_of_Triangle(1,3) == -1
