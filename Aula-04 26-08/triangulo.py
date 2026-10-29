""" 
3 - Escreva um programa que leia tres valores correspondentes aos tres lados de 
    um triangulo e determine se ele é isósceles, escaleno ou equilátero """

def main():
    lado1 = int(input("Digite o valor do lado 1: "))
    lado2 = int(input("Digite o valor do lado 2: "))
    lado3 = int(input("Digite o valor do lado 3: "))

    if((lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2)):
        if(lado1 == lado2 and lado2 == lado3):
            print("Triangulo equilatero")
        elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
            print("Triengulo Isóceles");
        else:
            print("Triangulo escaleno")
    else:
        print("Triangulo invalido!")

main()