"""
The Counting Sort algorithm sorts an array by counting the number of times each value occurs.
Counting Sort is fast when the range of possible values k is smaller than the number of values n

How it works:

    Create a new array for counting how many there are of the different values.
    Go through the array that needs to be sorted.
    For each value, count it by increasing the counting array at the corresponding index.
    After counting the values, go through the counting array to create the sorted array.
    For each count in the counting array, create the correct number of elements, with values that correspond to the counting array index.

So the time complexity for Count Sort is: O(n2)
"""

def countsort(array):
    max_val = max(array)
    count = [0] * (max_val+1)

    while len(array) > 0:
        num = array.pop()
        count[num] += 1
    
    for i in range(len(count)):
        while count[i] > 0:
            my_array.append(i)
            count[i] -= 1


    return array

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
sorted_array = countsort(my_array)     
print(f"After Count Sorting: {sorted_array}")