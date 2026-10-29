#6. Área do Círculo
#- Faça um programa que peça o raio de um círculo, calcule sua área e mostre o resultado. Considere π = 3.14159. (Fórmula: Área = π × raio²).

def main():
    pi = 3.14159
    print("----Area do Círculo----")
    raio = float(input("Digite o raio do círculo: "))

    area = pi * raio**2

    print("Area do circulo: %.2f", area)

main()