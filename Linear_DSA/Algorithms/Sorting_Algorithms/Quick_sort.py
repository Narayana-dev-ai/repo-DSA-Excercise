"""
As the name suggests, Quicksort is one of the fastest sorting algorithms.
The Quicksort algorithm takes an array of values, chooses one of the values as the 'pivot' element, and moves the other values so that lower values are on the left of the pivot element, and higher values are on the right of it.
Quicksort algorithm does the same operation recursively on the sub-arrays to the left and right side of the pivot element. This continues until the array is sorted.

How it works:

    Choose a value in the array to be the pivot element.
    Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
    Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
    Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.

So the time complexity for Quick Sort is: O(n log n)
"""

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
        
    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    
    if low < high:
        pivot_ind = partition(array, low, high)
        quicksort(array, low, pivot_ind-1)
        quicksort(array, pivot_ind+1, high)

quicksort(my_array)        
print(f"After Quick Sorting: {my_array}")