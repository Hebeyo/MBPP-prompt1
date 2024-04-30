"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to sort a list of elements using comb sort.
'''

def comb_sort(nums):
    n = len(nums)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1
        swapped = False
        i = 0
        while i + gap < n:
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swapped = True
            i += 1
    return nums


'''
Standard answer: 
def comb_sort(nums):
    shrink_fact = 1.3
    gaps = len(nums)
    swapped = True
    i = 0
    while gaps > 1 or swapped:
        gaps = int(float(gaps) / shrink_fact)
        swapped = False
        i = 0
        while gaps + i < len(nums):
            if nums[i] > nums[i+gaps]:
                nums[i], nums[i+gaps] = nums[i+gaps], nums[i]
                swapped = True
            i += 1
    return nums
'''
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
assert comb_sort([41, 32, 15, 19, 22]) == [15, 19, 22, 32, 41]
assert comb_sort([99, 15, 13, 47]) == [13, 15, 47, 99]
