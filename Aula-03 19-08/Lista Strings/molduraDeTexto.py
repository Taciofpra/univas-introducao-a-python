""" Exercício 6 - Moldura de texto
Leia uma palavra e apresente uma moldura utilizando o operador *.
Para a palavra PYTHON:
************
* PYTHON   *
************
O tamanho da linha superior deve ser calculado utilizando len()."""

def main():
    python = "Python"
    tamanho = len(python) + 4

    print("*"*tamanho)
    print("* "+python.upper()+" *")
    print("*"*tamanho)



main()