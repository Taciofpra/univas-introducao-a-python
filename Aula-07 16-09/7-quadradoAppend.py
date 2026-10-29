""" 7 - Crie uma lista vazia chamada quadrados. Escreva um laço for de 1 a 10 que calcule o
quadrado de cada número (n ** 2) e adicione o resultado na lista usando .append(). Exiba a
lista resultante no final """

def main():
    quadrados = []

    for i in range(1, 10):
        quadrados.append(i**2)

    for i in range(len(quadrados)):
        print(quadrados[i])

main()