"""
The Linear Search algorithm searches through an array and returns the index of the value it searches for.
If the array is already sorted, it is better to use the much faster Binary Search algorithm that we will explore on the next page.

A big difference between sorting algorithms and searching algorithms is that sorting algorithms modify the array, but searching algorithms leave the array unchanged.

How it works:

    Go through the array value by value from the start.
    Compare each value to check if it is equal to the value we are looking for.
    If the value is found, return the index of that value.
    If the end of the array is reached and the value is not found, return -1 to indicate that the value was not found.
    
the time complexity for Linear Search is O(n)

"""

def linearsearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    
    return -1

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
target = 22

result = linearsearch(my_array, target)

if result != -1:
    print(f"Value {target} found at index {result}")
else:
    print(f"Value {target} not found")