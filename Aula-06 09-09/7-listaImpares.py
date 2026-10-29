""" 7 - Crie uma lista com 6 nomes e imprima os nomes que estão nas posições impares da lista """

def main():
    lista = ["Tacio", "Gabriela", "Alessandra", "Julia", "Coré", "Carmem"]

    for i in range(6):
        if(i%2 != 0):
            print(lista[i], end=" ")

main()