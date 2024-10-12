"""
Given an array X[] of n integers where n &gt; 1, write a program to return an array product[] such that product[i] is equal to the product of all the elements of X except X[i].

Example:

Input: X[] = [2, 1, 3, 4], Output: product[] = [12, 24, 8, 6]

Explanation:
    Product except the 1st element = 1*3*4
    product except the 2nd element = 2*3*4
    Product except the 3rd element = 2*1*4
    product except the 4th element = 2*1*3
"""
array = [2, 1, 3, 4]
n = len(array)

def productArray(array, n):
    product = [0] * n
    product[0] = 1
    
    for i in range(1, n):
        product[i] = array[i-1] * product[i-1]
        
    suffixProduct = 1
    for i in range(n-1, -1, -1):
        product[i] = product[i]*suffixProduct
        suffixProduct *= array[i]
    
    return product

print(productArray(array, n))