""" 8 - análise de um aluno
Faça um programa que leia:
•	nome do aluno;
•	idade;
•	nota 1;
•	nota 2;
•	nota 3.
Calcule a média das três notas.
Depois apresente:
Nome:
Idade:
Nota 1:
Nota 2:
Nota 3:
Média:
Imprima a resposta
 """

def main():
    print("Analise de um aluno\n")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade:"))
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))

    media = (nota1 + nota2 + nota3)/3
    
    print("Nome: ", nome)
    print("Idade: ", idade)
    print("Nota 1: ", nota1)
    print("Nota 2: ", nota2)
    print("Nota 3: ", nota3)
    print("Media: ", media)

main()