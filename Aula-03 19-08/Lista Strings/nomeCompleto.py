""" Exercício 4 - Nome completo
Leia o primeiro nome e o sobrenome de uma pessoa separadamente.
Depois construa o nome completo utilizando o operador +.
 """

def main():
    nome = input("Digite seu primeiro nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    nomeCompleto = nome + " " + sobrenome

    print("Nome completo:", nomeCompleto)

main()