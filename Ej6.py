matriz= [[1,2,3,4],
         [5,6,7,8],
         [1,2,3,4],
         [5,6,7,8]]
def suma_diagonales(matriz):
    firstDiagonal= 0
    secondDiagonal= 0
    for i in range(len(matriz)):
        firstDiagonal += matriz[i][i]
    for i in range(len(matriz)):
        secondDiagonal += [i][len(matriz)-i-1]
    return firstDiagonal,secondDiagonal