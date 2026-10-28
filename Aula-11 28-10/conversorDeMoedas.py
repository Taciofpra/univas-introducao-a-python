""" Enunciado: Escreva uma função chamada converter_dolar_para_real que receba o valor 
em dólares e a cotação atual do dólar como parâmetros. A função deve calcular e 
retornar o valor equivalente em Reais. Teste a função passando o valor de uma 
compra de $50 dólares. """

def converter_dolar_para_real(Dolar):
    return Dolar * 5.58

def main():
    dolar = float(input("Digite um valor em dólares: "))

    real = converter_dolar_para_real(dolar)

    print("Valor convertido: R$ %.2f" % real)


main()