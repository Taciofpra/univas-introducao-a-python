#4 - Crie um programa que e imprima na tela os números impares de 1 a 100, utilizando while

#Funçao main
def main():
    print("-------------------------------")
    print("--Numeros impares de 1 a 100---")
    print("-------------------------------\n")

    i = 1
    while(i < 100):
        if(i % 2 != 0):
            print(i)

        i += 1

    print("Fim!")

#chamando a Main
main()