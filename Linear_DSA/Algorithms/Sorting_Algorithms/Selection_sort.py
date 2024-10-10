"""
The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.
The algorithm looks through the array again and again, moving the next lowest values to the front, until the array is sorted.

How it works:

    Go through the array to find the lowest value.
    Move the lowest value to the front of the unsorted part of the array.
    Go through the array again as many times as there are values in the array.

So the time complexity for Selection Sort is: O(n2)
"""

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)

for i in range(n-1):
    min_ind = i
    for j in range(i+1,n):
        if my_array[j] < my_array[min_ind]:
            min_ind = j
    
    my_array[i], my_array[min_ind] = my_array[min_ind], my_array[i]
        
print(f"After Selection Sorting: {my_array}")