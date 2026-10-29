""" 2 - Peça ao usuário para digitar um número inteiro. Utilize um laço for com range(1, 11) para
exibir a tabuada desse número (de 1 a 10) """

def main():

    num = int(input("Digite um numero: "))
    for i in range(1, 11):
        print(num,"*", i, "=",num*i)

main()