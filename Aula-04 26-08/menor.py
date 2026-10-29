""" 
2 - Escreva um programa que dados tres números inteiros, imprima o menor deles
 """

def main():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    num3 = int(input("Digite o terceiro numero: "))

    if(num1 < num2 and num1 < num3):
        print("Menor:",num1)
    elif(num2 < num3):
        print("Menor:",num2)
    else:
        print("Menor:",num3)

main()