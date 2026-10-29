""" 5 - Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido """

def main():
    numero = int(input("Digite um numero: "))

    print("Tabuada do", numero, ":")

    for i in range(10):
        print(i+1 ," *", numero," = ",(i+1)*numero)

main()