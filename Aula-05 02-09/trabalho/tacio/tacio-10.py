""" 10 - Crie um programa que armazene dois números em variáveis. Calcule e exiba a soma,
subtração, multiplicação e divisão desses números. ( +, -, *, /) """

#Funçao main
def main():
    print("-------------------------")
    print("---Calculadora Simples---")
    print("-------------------------\n")    

    #entrada de dados
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))

    #Exibindo resultados formatados com até 2 casas decimais
    #não exibe casas decimais em caso de numero Inteiro
    print(f"{a:g} + {b:g} = {a+b:.3g}")
    print(f"{a:g} - {b:g} = {a-b:.3g}")
    print(f"{a:g} * {b:g} = {a*b:.3g}")
    print(f"{a:g} / {b:g} = {a/b:.3g}")

#Chamando a main
main()