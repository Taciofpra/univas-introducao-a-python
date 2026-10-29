""" 4 - Escreva um programa que leia uma idade e se a pessoa tem carteira ou não se a pessoa
tiver 18 anos ou mais e possuir carteira, ela pode dirigir, qualquer outra informação, ela não
pode dirigir. """

def main():
    idade = int(input("Digite sua idade: "))
    carteira = input("Você possui carteira? S ou N: ").lower()

    if(idade >=18 and carteira == 's'):
        print("Pode dirigir.")
    else:
        print("Não pode dirigir.")

main()