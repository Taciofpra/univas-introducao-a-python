""" 9 - Crie um programa que leia o nome, idade e altura de uma pessoa, e exiba a seguinte
mensagem:
Ex: Maria tem 22 anos e mede 1.68 metros """

#Função main
def main():
    print("--------------")
    print("---Saudação---")
    print("--------------\n")

    #entrada de dados:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))

    #saida de dados
    print(nome,"tem",idade,"anos e mede %.2f"%altura,"metros")

#Chamando a Main
main()