""" 8 - Faça um programa em Python que peça para o usuário entrar com um número de 1 a 10 e
mostre a tabuada de 1 a 10 desse número. """

#Função main
def main():
    print("-------------")
    print("---Tabuada---")
    print("-------------")

    #inicializando variaveis
    num = 0
    i=1

    #entrada e validador de dados
    while(num<1 or num > 10):
        num = int(input("Digite um numero de 1 a 10: "))
        if(num<1 or num > 10):
            print("Valor invalido!")

    print()
    print("--- Tabuada do", num,"---")

    #processamento e saida de dados
    while(i <= 10):
        print(num,"*",i,"=",num*i)
        i += 1
    print("--------------------")   

#chamando a Main  
main()
