"""
The Binary Search algorithm searches through an array and returns the index of the value it searches for.
Binary Search is much faster than Linear Search, but requires a sorted array to work.

How it works:

    Check the value in the center of the array.
    If the target value is lower, search the left half of the array. If the target value is higher, search the right half.
    Continue step 1 and 2 for the new reduced part of the array until the target value is found or until the search area is empty.
    If the value is found, return the target value index. If the target value is not found, return -1.
    
the time complexity for Binary Search is O(log2n)
"""

def binarysearch(array, target):
    left = 0
    right = len(array) -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] == target:
            return mid
        
        if array[mid] < target :
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def binarySearchRecursive(array, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if array[mid] == target:
        return mid
    elif target > array[mid]:
        return binarySearchRecursive(array, mid+1, high, target)
    elif target < array[mid]:
        return binarySearchRecursive(array, low, mid-1, target)
    
    
def displayOutput(result, myTarget):
    if result != -1:
        print(f"Value {myTarget} found at index {result}")
    else:
        print(f"Target not found in array.")
 
myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

displayOutput(binarysearch(myArray, 15), 15)
displayOutput(binarySearchRecursive(myArray, 0, len(myArray)-1, 1), 1)


