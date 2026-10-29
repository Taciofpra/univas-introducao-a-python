""" Exercício 9 - Índices negativos
Leia uma palavra e apresente:
•	o primeiro caractere utilizando índice positivo;
•	o último caractere utilizando índice negativo;
•	o segundo caractere utilizando índice positivo;
•	o penúltimo caractere utilizando índice negativo.
 """

def main():
    palavra = input("Digite uma palavra: ")

    print(palavra[0])
    print(palavra[-1])
    print(palavra[1])
    print(palavra[-2])

main()