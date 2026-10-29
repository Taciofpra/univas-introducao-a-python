#5. Conversor de Medidas
#- Escreva um programa que leia um valor em metros e o exiba convertido para centímetros (Dica: 1 metro = 100 centímetros).

def main():
    print("----Conversor de medidas----")

    metros = float(input("Digite uma medida em metros: "))
    centimetros = metros * 100

    print("Metros:", metros)
    print("Centimetros:", centimetros)

main()