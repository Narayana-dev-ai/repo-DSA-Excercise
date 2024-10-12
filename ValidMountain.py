"""
Given an array X of n integers, write a program to check if the array is a valid mountain array or not.
The array X is a mountain array if and only if n >= 3 and there exists some i (0 < i < n -1) such that: X[0] < X[1] <...< X[i-1] < X[i] and X[i] > X[i+1] > ...> X[n-1]. 
In other words, the array is a valid mountain when it is first strictly increasing and then strictly decreasing.

Examples::

Input: X[] = [5, 2, 1, 4], Output: False
Input: X[] = [5, 8, 8], Output: False
Input: X[] = [1, 2, 6, 5, 3], Output: True
"""

mountains = [1, 2, 6, 5, 3]
n = 5

def checkMountains(array, n):
    left = 0
    right = n-1
    
    while left < n-1 and array[left] < array[left+1]:
        left +=1
    
    while right > 0 and array[right-1] > array[right]:
        right -=1
    
    if left > 0 and right < n-1 and left == right:
        return True
    else:
        return False

print(checkMountains(mountains, n))