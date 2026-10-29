""" Exercício 3 - Mensagem personalizada
Leia:
nome do aluno;
curso;
período.
Depois construa uma mensagem semelhante a:
Carlos é aluno do 1º período do curso de Sistemas de Informação.
 """

def main():
    nome = input("Digite seu nome: ")
    curso = input("Digite seu curso: ")
    periodo = input("Digite seu periodo atual: ")

    print(nome,"é aluno do", periodo,"º periodo do curso de", curso)

main()