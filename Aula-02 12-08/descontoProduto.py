
#9. Desconto de Produto
#- Faça um programa que receba o preço de um produto e o percentual de desconto. 
#  Calcule e mostre o valor do desconto e o preço final a ser pago.

def main():
    print("----Desconto de Produto----")

    preco = float(input("Digite o preço do produo: "))
    desconto = int(input("Digite o desconto concedido: "))

    total = preco * (1-(desconto/100))

    print("Valor final: ", total)

main()