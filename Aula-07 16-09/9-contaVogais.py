""" 9 - Peça ao usuário para digitar uma palavra. Utilize o laço for para percorrer a string caractere
por caractere e contar quantas vogais (a, e, i, o, u) ela possui. """

def main():

    contaVogais = 0

    palavra = input("Digite uma palavra: ").lower()
    
    for char in palavra:
        if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
            contaVogais += 1

    print("Total de vogais:",contaVogais)

main()