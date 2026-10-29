""" 3 - Crie uma lista com 5 nomes de disciplinas do seu curso. Percorra a lista usando for e exiba
cada disciplina com a frase: "Disciplina: [Nome da Disciplina]". """

def main():
    disciplina = ["sistemasEmbarcados", "UML", "introducaoAProgramacao", "iaAplicada", "IntroducaoApython"]

    tam = len(disciplina)
    for i in range(0, tam):
        print("Disciplina: ", disciplina[i])

main()