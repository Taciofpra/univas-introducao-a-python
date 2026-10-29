#8. Conversor de Temperatura
#- Escreva um programa que peça a temperatura em graus Fahrenheit, 
#  transforme e mostre a temperatura em graus Celsius. (Fórmula: \(C = 5 \times \frac{F - 32}{9}\)).

def main():
    print("----Conversos Fahrenheit -> Celsius----")
    fTemperatura = float(input("Digite a temperatura em Fahrenheit: "))

    cTemperatura = 5* ((fTemperatura - 32) / 9)

    print("Fahrenheit: ", fTemperatura)
    print("Celsius: ", cTemperatura)

main()