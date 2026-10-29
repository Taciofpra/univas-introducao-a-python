""" 5 - a lista numeros = [12, 5, 8, 21, 14, 3, 9, 18], percorra-a utilizando for e conte quantos
números são pares. Imprima o total ao final. """

def main():
    numeros = [12, 5, 8, 21, 14, 3, 9, 18]
    pares = 0

    for i in range(len(numeros)):
        if(numeros[i] % 2 == 0):
            pares += 1

    print("Total de pares:", pares)

    
main()