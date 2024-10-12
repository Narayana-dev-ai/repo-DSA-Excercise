"""
Given a Roman numeral, write a program to find its corresponding decimal value. Roman numerals are represented by seven different symbols:

Input: XL, Output: 40
Input: MCMXCIV, Output: 1994
"""

roman = "MCMXCIV"
n = len(roman)

def mapping(letter):
    if letter == "I":
        return 1
    if letter == "V":
        return 5
    if letter == "X":
        return 10
    if letter == "L":
        return 50
    if letter == "C":
        return 100
    if letter == "D":
        return 500
    if letter == "M":
        return 1000
    
    return -1


def romanToInteger(roman, n):
    output = 0
    
    for i in range(n):
        currentVal = mapping(roman[i])
        
        if i+1 < n:
            nextVal = mapping(roman[i+1])
            
            if currentVal > nextVal:
                output += currentVal
            else:
                output -= currentVal
        else:
            output += currentVal
    return output
    
    
print(romanToInteger(roman, n))