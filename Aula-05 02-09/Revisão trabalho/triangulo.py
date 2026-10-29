""" 
3 - Escreva um programa que leia tres valores correspondentes aos tres lados de 
    um triangulo e determine se ele é isósceles, escaleno ou equilátero """


def main():
    print("------------------------")
    print("---Verifica Triangulo---")  
    print("------------------------")

    
    ladoA = int(input("Digite o valor do lado A: "))
    ladoB = int(input("Digite o valor do lado B: "))
    ladoC = int(input("Digite o valor do lado C: "))

    if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):
        if(ladoA == ladoB) and (ladoB == ladoC):
            print("Triangulo Equilátero!")
        elif (ladoA == ladoB) or (ladoB == ladoC) or (ladoA == ladoC):
            print("Triangulo Isóceles!")
        else:
            print("Triangulo Escaleno!")
    else:
        print("Triangulo Invalido!")



main()