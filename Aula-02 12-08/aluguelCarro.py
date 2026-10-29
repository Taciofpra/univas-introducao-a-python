#10. Aluguel de Carro
#- Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado 
#  e a quantidade de dias pelos quais ele foi alugado. 
#  Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

def main():
    print("----Aluguel de carro----\n")

    km=float(input("Digite quantos Quilometros foram percorridos: "))
    dias = int(input("Digite a quantidade de dias da locação: "))

    preco = dias*60 + km * 0.15

    print("Preço da locação: %.2f" % preco)
    
main()