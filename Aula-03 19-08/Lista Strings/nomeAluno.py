""" Exercício 1 - Nome do aluno
Faça um programa que solicite o nome de um aluno e apresente:
•	o nome informado;
•	a quantidade de caracteres do nome.
 """

def main():
    nome = input("Digite seu nome: ")
    tamanho = len(nome)

    print("Nome:", nome)
    print("Caracteres:", tamanho)

main()