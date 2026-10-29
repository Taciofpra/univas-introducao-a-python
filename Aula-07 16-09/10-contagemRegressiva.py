""" 10 - Utilize a função range() no laço for para imprimir uma contagem regressiva de 10 até 1 e,
ao final, exiba a mensagem "Fim da contagem!" """

def main():
    for i in range(10, 0, -1):
        print(i, end=" ")

main()