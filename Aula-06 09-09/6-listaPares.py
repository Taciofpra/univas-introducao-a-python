""" 6 - Crie uma lista com 8 elementos e imprima os elementos que estão nas posições pares da lista """

def main():
    lista = [0, 1, 2, 3, 4, 5, 6, 7]

    for i in range(8):
        if(i%2 ==0):
            print(lista[i], end=" ")

main()