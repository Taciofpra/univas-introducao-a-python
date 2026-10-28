""" Enunciado: Desenvolva uma função chamada avaliar_media que receba três notas de 
um aluno. A função deve calcular a média aritmética simples dessas notas. Se a
média for maior ou igual a 7.0, retorne a string "Aprovado". Se for menor, retorne "Exame". """

def avalia_media(Notas):
    media = 0

    for i in range(len(Notas)):
        media = media + Notas[i]
 
    if media/3 >= 7.0:
        return "Aprovado"
    else:
        return "Exame"

def main():
    notas = [3]

    for i in range(3):
        nota = float(input(f"digite a {i+1}ª nota: "))
        notas.append(nota)

    status = avalia_media(notas)

    print("Status do aluno:", status)





main()