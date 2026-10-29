#6 - Crie um programa que peça para digitar um número e retorne se o número é par ou impar

#Funçao main
def main():
    print("--------------------------")
    print("--Verifica par ou impar---")
    print("--------------------------\n")
    #entrada de dados
    num = int(input("Digite um número: "))

    #processamento e saida de dados
    if(num % 2 == 0):
        print("O numero", num,"é par!")
    else: 
        print("O numero", num,"é impar!")

#chamando a Main
main()