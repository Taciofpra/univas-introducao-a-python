""" 6 Dada a tupla dias = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta"), utilize o laço for com
enumerate() para exibir os dias acompanhados de um número de ordem (ex: 1 - Segunda, 2 -
Terça, etc.). """

def main():
    dias = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta")

    for indice, dia in enumerate(dias, start=1):
        print(indice,"-", dia)

main()