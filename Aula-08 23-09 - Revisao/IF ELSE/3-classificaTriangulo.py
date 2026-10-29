""" 3 - Escreva um programa que leia três valores correspondentes aos três lados de um triangulo
e determine se ele é isósceles, escaleno ou equilátero """

def main():

    print("Classificando triangulo")
    l1 = int(input("Digite o valor do lado 1: "))
    l2 = int(input("Digite o valor do lado 2: "))
    l3 = int(input("Digite o valor do lado 3: "))

    if(l1+l2>l3 and l2+l3>l1 and l1+l3>l2):
        if(l1 == l2 and l2 == l3):
            print("Triangulo Equilatero")
        elif(l1 == l2 or l2 == l3 or l1 == l3):
            print("Triangulo isóceles")
        else:
            print("Triangulo escaleno.")
    else:
        print("Triangulo invalido.")
        

main()