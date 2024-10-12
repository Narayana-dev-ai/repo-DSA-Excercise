"""
Given an n x n square matrix, write a program to rotate the matrix by 90 degrees in the anti-clockwise direction. The goal is to perform the matrix rotation in place, meaning we need to rotate the matrix without using extra space.

Example:

Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]], Output: [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matrix[0])

def matrixRotation(matrixx, n):
    for i in range(n // 2):
        for j in range(i, n-i-1):
            temp = matrixx[i][j]
            matrixx[i][j] = matrixx[j][n-1-i]
            matrixx[j][n-1-i] = matrixx[n-1-i][n-1-j]
            matrixx[n-1-i][n-1-j] = matrixx[n-1-j][i]
            matrixx[n-1-j][i] = temp
            
    return matrixx

print(matrixRotation(matrix, n))