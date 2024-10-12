"""
Write a program to find the equilibrium index of an array. The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

Input: A[] = [-7, 1, 5, 2, -4, 3, 0], Output: 3

Explanation: 3 is an equilibrium index, i.e., A[0] + A[1] + A[2] = A[4] + A[5] + A[6] = -1.
"""
array = [0, 1, 3, -2, -1]
n = len(array)

def findEquilibriumIndex(array, n):
    totalSum = 0
    leftSum =0
    
    for i in range(n):
        totalSum += array[i]
        
    for i in range(n):
        rightSum = totalSum - leftSum - array[i]
        if rightSum == leftSum:
            return i
        leftSum += array[i]
    
    return -1

print(findEquilibriumIndex(array, n))