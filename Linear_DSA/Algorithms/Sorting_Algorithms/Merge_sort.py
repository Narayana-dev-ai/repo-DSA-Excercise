"""
The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays, and then building the array back together the correct way so that it is sorted.

Divide: The algorithm starts with breaking up the array into smaller and smaller pieces until one such sub-array only consists of one element.

Conquer: The algorithm merges the small pieces of the array back together by putting the lowest values first, resulting in a sorted array.

The breaking down and building up of the array to sort the array is done recursively.

How it works:

    Divide the unsorted array into two sub-arrays, half the size of the original.
    Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
    Merge two sub-arrays together by always putting the lowest value first.
    Keep merging until there are no sub-arrays left.

So the time complexity for Quick Sort is: O(n. log n)
"""

def mergesort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left_arr = array[:mid]
    right_arr = array[mid:]

    sortLeft = mergesort(left_arr)
    sortRight = mergesort(right_arr)

    return merge(sortLeft, sortRight)

def merge(left, right):
    result = []
    i=j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])


    return result
   

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
sorted_array = mergesort(my_array)     
print(f"After Merge Sorting: {sorted_array}")