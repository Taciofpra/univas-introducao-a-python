""" Exercício 5 - Repetição de strings
Leia uma palavra.
Apresente essa palavra:
•	uma vez;
•	duas vezes;
•	três vezes;
•	cinco vezes.
Utilize o operador *."""


def main():
    palavra = input("Digite uma palavra: ")

    print(palavra)
    print((palavra + " ") * 2)
    print((palavra + " ") * 3)
    print((palavra + " ") * 4)
    print((palavra + " ") * 5)

main()