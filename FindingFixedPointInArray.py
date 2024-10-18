"""
Write a program that returns the index of a fixed point in the given sorted array of distinct integers. A fixed point is an index i such that X[i] is equal to i. If a fixed point is found, we should return its index. If no fixed point is found, we should return -1. Note that the integers in the array may be both positive and negative.

Examples:
Input: X[] = [-4, -2, 0, 1, 4, 6, 7], Output: 4
"""

def findFixedPointInSortedArray(array, low, high):
    if low <= high:
        mid = (low + high) // 2
        if array[mid] == mid:
            return mid
        elif mid < array[mid]:
            return findFixedPointInSortedArray(array, low, mid-1)
        else:
            return findFixedPointInSortedArray(array, mid+1, high)
    return -1


array = [-4, -2, 0, 1, 4, 6, 7]
print(findFixedPointInSortedArray(array, 0, len(array)))