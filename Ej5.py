matriz=[[4,98,30],
        [3,8,17],
        [18,2007,50]]
def suma_filas(matriz):
    firstlist=[]
    for i in matriz:
        numbers= sum(i)
        firstlist.append(numbers)
    return firstlist
def suma_columnas(matriz):
    secondlist=[]
    for i in range(len(matriz[0])):
        numbers=0
        for j in range(len(matriz)):
            numbers+=matriz[j][i]
        secondlist.append(numbers)
    return secondlist
def transpuesta(matriz):
    thirdlist= []
    for i in range(len(matriz[0])):
        fila=[]
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        thirdlist.append(fila)
    return thirdlist

print(suma_filas(matriz))
print(suma_columnas(matriz))
print(transpuesta(matriz))