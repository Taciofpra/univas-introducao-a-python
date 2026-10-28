""" Enunciado: Um engenheiro precisa calcular a área de terrenos retangulares. Escreva 
uma função chamada calcular_area que receba a largura e o comprimento (em metros) 
como parâmetros. A função deve calcular a área (largura × comprimento) e retornar 
(return) o valor obtido. Fora da função, exiba o resultado na tela. """

def calcular_area(l, c):
    return l * c


def main():
    largura = float(input("Digite a Largura: "))
    comprimento = float(input("Digite o comprimento: "))

    area = calcular_area(largura, comprimento)

    print("Area do terreno: ", area)

main()