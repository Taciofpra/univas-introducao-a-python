""" 4 - Dada a lista de inteiros valores = [10, 20, 30, 40, 50], utilize um laço for para calcular e exibir
a soma de todos os elementos da lista (sem usar a função embutida sum()). """

def main():
    lista = [10, 20, 30, 40, 50]
    res = 0

    for i in range(len(lista)):
        res += lista[i]

    print("Total =", res)

main()