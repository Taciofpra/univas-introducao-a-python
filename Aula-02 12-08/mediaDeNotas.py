#4. Média de Notas
#- Crie um programa que receba 4 notas bimestrais de um aluno, calcule a média aritmética e imprima o resultado na tela.

def main():
    print("----Calculando media de 4 notas----")

    nota1=float(input("Digite o valor da nota 1: "))
    nota2=float(input("Digite o valor da nota 2: "))
    nota3=float(input("Digite o valor da nota 3: "))
    nota4=float(input("Digite o valor da nota 4: "))

    media = (nota1 + nota2 + nota3 + nota4)/4

    print("Media das notas: ", media)
    
main()