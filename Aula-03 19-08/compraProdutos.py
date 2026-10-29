""" 7 - Compra de produtos
Uma pessoa comprou três produtos.
Leia:
•	preço do produto 1;
•	preço do produto 2;
•	preço do produto 3.
Calcule:
•	o valor total da compra;
•	o valor médio dos produtos;
Imprima a resposta """

def main():
    preco1 = float(input("Digite o preço do produto 1: "))
    preco2 = float(input("Digite o preço do produto 2: "))
    preco3 = float(input("Digite o preço do produto 3: "))

    total = preco1 + preco2 + preco3
    media = total/3

    print("Total da compra: %.2f"% total)
    print("Media: %.2f"% media)
    
main()