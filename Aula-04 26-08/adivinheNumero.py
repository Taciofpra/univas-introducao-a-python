""" 6 - Faça um programa que receba um número digitado pelo usuário e verifique sé é igual a um numero
    colocado dentro do código. se sim imprimir (venceu) se não pedir pra digitar outro numero até o usuário 
    acertar. """

def main():
    numero = 14

    tentativa = int(input("Tente adivinhar o numero secreto! (0 a 100): "))

    while(tentativa != numero):
        tentativa = int(input("Tente novamente: "))

    print("Você venceu!")

main()