""" 2 - Escreva um programa que dados três números inteiros, imprima o menor deles """

def main():
    numeros = []

    for i in range(3):
        numeros.append(int(input("Digite um numero: ")))

    menor = numeros[0]

    for i in range(1, len(numeros)):
        if(numeros[i] < menor):
            menor = numeros[i]

    print("Menor: ", menor)

main()