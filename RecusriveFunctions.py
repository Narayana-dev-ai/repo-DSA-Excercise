def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
def reverseArrayRecusrively(array, low, high):
    if low > high:
        return 
    else:
        array[low], array[high] = array[high], array[low]
        return reverseArrayRecusrively(array, low+1, high-1)
    
def fibanaaciElement(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibanaaciElement(n-1) + fibanaaciElement(n-2)

def findGCD(a, b):
    if a == b:
        return a
    elif a > b:
        return findGCD(a-b, b)
    else:
        return findGCD(a, b-a)
    
    
print(factorial(5))
array = [1,2,3,4,5]
reverseArrayRecusrively(array, 0, 4)
print(array)
print(fibanaaciElement(6))
print(findGCD(36, 60))