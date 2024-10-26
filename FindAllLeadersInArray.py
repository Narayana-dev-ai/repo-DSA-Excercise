"""
Given an integer array X[] of size n, write a program to find all the leaders in the array X[]. An element is a leader if it is strictly greater than all the elements to its right side.
    The last element of an array is a leader by default.
    The largest element of an array is also a leader by default.
    Suppose all the array elements are unique.
    Ordering in the output doesn’t matter.
Examples::

Input:
    X[] = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]

Explanation:&nbsp;Element 2 is the rightmost element, so it is a leader by default. 17 and 5 are also leader elements because they are greater than all the elements on their right side.
"""

leaders = [16, 17, 4, 3, 5, 2]
n = 6

def findLeaders(array, n):
    list = []
    maxFromRight = array[n-1]
    list.append(maxFromRight)
    
    for i in range(n-2, -1, -1):
        if array[i] > maxFromRight:
            maxFromRight = array[i]
            list.insert(0, maxFromRight)
    
    return list

print(findLeaders(leaders, n))