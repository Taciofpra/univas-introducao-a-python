#3. Soma de Dois Números
#- Desenvolva um programa que peça dois números inteiros ao usuário, calcule a soma entre eles e mostre o resultado.

def main():
    print("---Soma de Dois Numeros----")
    num1 = int(input("Digite o Valor do primeiro numero: "))
    num2 = int(input("Digite o valor do segundo numero: "))

    total = num1 + num2

    print(num1," + ", num2," = ", total)

    
main()