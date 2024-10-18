"""
You are given an array of integers that is initially increasing and then decreasing, find the maximum value in the array. Hint: keep in mind the corner cases.
https://www.enjoyalgorithms.com/blog/find-maximum-in-first-increasing-and-then-decreasing-array

Examples:
Input: X[] = [18, 110, 210, 452, 810, 500, 101, 13], Output: 810
"""

def findMaximum(array, low, high):
    if low == high:
        return array[low]
    
    if high == low + 1 and array[low] >= array[high]:
        return array[low]
    if high == low + 1 and array[low] < array[high]:
        return array[high]
    
    mid = low + (high-low) // 2
    if array[mid] > array[mid+1] and array[mid] > array[mid-1]:
        return array[mid]
    
    if array[mid] > array[mid+1] and array[mid] < array[mid-1]:
        return findMaximum(array, low, mid-1)
    else:
        return findMaximum(array, mid+1, high) 
    
    
array = [1, 2, 3, 4, 5]
print(findMaximum(array, 0, len(array)-1))