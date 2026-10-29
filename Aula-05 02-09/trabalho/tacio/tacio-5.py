#5 - Crie um programa que mostre se o número é par ou ímpar e mostre na tela

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