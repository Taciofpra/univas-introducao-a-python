""" Exercício 10 — Fatiamento
Considere:
texto = "SISTEMAS DE INFORMACAO"
Utilize fatiamento para obter:
SISTEMAS
DE
INFORMACAO
 """

def main():
    texto = "SISTEMAS DE INFORMAÇÃO"

    textoSeparado = texto.split()

    for word in textoSeparado:
        print(word)


main()