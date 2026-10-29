""" 5 - Crie uma lista com 6 elementos e imprima de tras para frente na tela """

def main():
    lista = [1, 2, 3, 4, 5, 6]

    for i in range(5, -1, -1):
        print(lista[i], end = " ")

main()