""" 1 - Escreva um programa que verifica se um aluno foi aprovado ou não na escola
obs: aprovação >= a 60
exame >= 30 e < 60
reprovado < que 30 """

def main(): 
    nota = int(input("Digite sua nota: "))

    if( nota>= 60):
        print("Aprovado!")
    elif (nota >= 30):
        print("Exame.")
    else:
        print("Reprovado.")


main()