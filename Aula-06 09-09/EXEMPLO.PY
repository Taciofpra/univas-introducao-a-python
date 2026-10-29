

def main():
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    lista3 = [7, 8, 9]

    matriz = [lista1, lista2, lista3]

    lista1.append(4)

    for i in range(3):
        for j in range(3):
            if(i == j):
                print(matriz[i][j], end=" ")

main()