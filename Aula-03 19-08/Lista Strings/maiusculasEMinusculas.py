""" Exercício 2 - Nome em maiúsculas e minúsculas
Leia o nome de uma pessoa.
Apresente o nome: 
•	exatamente como foi digitado;
•	em letras maiúsculas;
•	em letras minúsculas.
 """

def main():
    nome = input("Digite seu nome: ")

    print(nome.upper())
    print(nome.lower())

main()