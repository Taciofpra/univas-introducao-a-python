""" 4 - Escreva um programa que leia uma idade e se a pessoa tem carteira ou não.
    se a pessoa tiver 18 anos ou mais e possuir carteira, ela pode dirigir, qualquer 
    outra informação, ela não pode dirigir. """

def main():
    idade = int(input("Digite sua idade: "))
    carteira = input("Possui carteira? S ou N: ")

    if(idade>=18 and (carteira == "S" or carteira == "s")):
        print("Pode dirigir")
    else:
        print("Ainda não pode dirigir!")

        
main()