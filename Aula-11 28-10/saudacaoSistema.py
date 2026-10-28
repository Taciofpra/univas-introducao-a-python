""" Enunciado: Crie uma função chamada saudar_aluno que receba o nome de um aluno 
como parâmetro. A função deve exibir na tela uma mensagem de boas-vindas 
personalizada, como: "Olá, [Nome], bem-vindo ao curso de Sistemas de Informação!". """

def saudar_aluno(Nome):
    print("Ola", Nome,"bem-vindo ao curso de Sistemas de Informação")


def main():
    nome = input("Digite seu nome: ")

    saudar_aluno(nome)

main()