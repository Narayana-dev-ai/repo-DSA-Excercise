"""
Given an array&nbsp;X[]&nbsp;of size&nbsp;n, we need to find the maximum and minimum elements present in the array. Our algorithm should make the minimum number of comparisons.

Input: X[] = [4, 2, 0, 8, 20, 9, 2], Output: max = 20, min = 0
"""
array = [4, 2, 0, 8, 20, 9, 2, 30]
n = len(array)

def findMinMaxOfArray(array, n):
    maxVal=minVal=i=0
    if n % 2 != 0:
        maxVal = array[0]
        minVal = array[0]
        i = 1
    else:
        if array[0] < array[1]:
            maxVal = array[1]
            minVal = array[0]
        else:
            maxVal = array[0]
            minVal = array[1]
        i = 2
    
    while i < n:
        if array[i] < array[i+1]:
            if array[i] < minVal:
                minVal = array[i]
            if array[i+1] > maxVal:
                maxVal = array[i+1]
        else:
            if array[i] > maxVal:
                maxVal = array[i]
            if array[i+1] < minVal:
                minVal = array[i+1]
            
        i += 2
    
    return {"max": maxVal, "min": minVal}

print(findMinMaxOfArray(array, n))