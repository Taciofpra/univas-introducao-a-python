""" 7 – Escreva um programa que leia três valores correspondentes aos três lados de um triangulo
e determine se ele é isósceles, escaleno ou equilátero. """

#Função main
def main():
    print("---------------------------------------------")
    print("---Validador e classificador de Triangulos---")
    print("---------------------------------------------")

    #entrada de dados
    ladoA = int(input("Digite o valor do ladon A: "))
    ladoB = int(input("Digite o valor do ladon B: "))
    ladoC = int(input("Digite o valor do ladon C: "))

    #Processamento e saida de dados
    if(ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):
        #Triangulo valido
        if(ladoA == ladoB) and (ladoB == ladoC):
            print("O Triangulo", ladoA, ladoB, ladoC,"é equilátero!")
        elif(ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
            print("O Triangulo", ladoA, ladoB, ladoC,"é isóceles!.")
        else:
            print("O Triangulo", ladoA, ladoB, ladoC,"é escaleno.")
    else:
        #Triangulo invalido
        print("Triangulo inválido!")

#chamando a Main      
main()