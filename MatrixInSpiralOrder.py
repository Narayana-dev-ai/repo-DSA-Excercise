matrix = [
    [3, 6, 9], 
    [2, 5, 8], 
    [1, 4, 7]
]
x = 3
y = 3

def printMatrixSpiralOrder(matrixx, rowStart, colStart, rowEnd, colEnd):
    
    if rowStart > rowEnd or colStart > colEnd:
        return
    
    for i in range(colEnd):
        print(matrixx[rowStart][i], end=" ")
        
    for i in range(rowStart+1, rowEnd):
        print(matrixx[i][colEnd-1], end=" ")
        
    if rowEnd != rowStart:
        for i in range(colEnd-1, colStart, -1):
            print(matrixx[rowEnd-1][i-1], end=" ")
    if colEnd != colStart:
        for i in range(rowEnd-1, rowStart, -1):
            print(matrixx[i-1][colStart], end=" ")
        
    printMatrixSpiralOrder(matrixx, rowStart+1, rowEnd-1, colStart+1, colEnd-1)

printMatrixSpiralOrder(matrix, 0, 0, x, y)