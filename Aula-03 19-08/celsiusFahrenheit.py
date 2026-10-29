""" 4 - Faça um programa que leia uma temperatura em graus Celsius e converta para Fahrenheit.
Utilize a fórmula:
F = (C × 9 / 5) + 32
Imprima a resposta
 """

def main():
    print("-----Conversor Celsius -> Fahrenheit-----")
    c = float(input("Digite a temperatura em Celsius: "))

    print("Celsius: ", c)
    print("Fahrenheit", (c*9/5)+32)

main()