"""
Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.
The word 'Bubble' comes from how this algorithm works, it makes the highest values 'bubble up'.

How it works:

    Go through the array, one value at a time.
    For each value, compare the value with the next value.
    If the value is higher than the next one, swap the values so that the highest value comes last.
    Go through the array as many times as there are values in the array.

So the time complexity for Bubble Sort is: O(n2)
"""

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)

for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print(f"After Bubble Sorting: {my_array}")